#!/usr/bin/env python3
"""
Phase 1 Report Generation Pipeline
Face → Features → KB Match → LLM → Report
"""

import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from prompts.face_personality_v1 import SYSTEM_PROMPT_V1, build_user_prompt
from knowledge.face_kb_v2 import get_knowledge_context
from deepseek_client import DeepSeekClient  # reuse existing client


class FaceReportGenerator:
    """AI face personality report generator"""
    
    def __init__(self):
        self.client = DeepSeekClient()
    
    async def generate(self, features: dict, stream: bool = False) -> dict:
        """
        Generate full report from facial features.
        
        Args:
            features: dict from MediaPipe extraction
            stream: if True, return streaming generator
        
        Returns:
            dict with keys: report, features, rules_matched, tokens_used
        """
        # 1. Build knowledge context
        kb_context = get_knowledge_context(features)
        
        # 2. Build user prompt
        user_prompt = build_user_prompt(features)
        
        # 3. Combine
        full_user_prompt = f"{kb_context}\n\n{user_prompt}"
        
        # 4. Call LLM
        if stream:
            return self.client.chat_stream(
                system=SYSTEM_PROMPT_V1,
                user=full_user_prompt,
                max_tokens=2000,
                temperature=0.7
            )
        
        response = await self.client.chat(
            system=SYSTEM_PROMPT_V1,
            user=full_user_prompt,
            max_tokens=2000,
            temperature=0.7
        )
        
        text, tokens = response  # Tuple[str, int]
        
        return {
            "report": text,
            "features": features,
            "rules_matched": len(list(self._count_rules(features))),
            "tokens_used": tokens,
            "model": "deepseek-chat",
        }
    
    def _count_rules(self, features):
        from knowledge.face_kb_v2 import match_features
        return match_features(features)


# Test
if __name__ == "__main__":
    gen = FaceReportGenerator()
    test_features = {
        "face_ratio": 1.32,
        "forehead_ratio": 0.36,
        "midface_ratio": 0.34,
        "lowerface_ratio": 0.30,
        "eye_distance": 0.31,
        "nose_width": 0.15,
        "jaw_angle": 110,
        "brow_angle": 15,
        "gender": "女",
        "age_range": "25-35",
        "concern": "职业发展"
    }
    print("Generating report...")
    result = gen.generate(test_features)
    print(f"Rules matched: {result['rules_matched']}")
    print(f"Tokens: {result['tokens_used']}")
    print(f"\n{'='*60}\nREPORT\n{'='*60}")
    print(result['report'][:500] + "...")
