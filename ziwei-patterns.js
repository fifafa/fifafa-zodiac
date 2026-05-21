/*
 * P0 FIX: Add real detectPatterns function to ziwei.js
 * Ported from patterns.ts — 12 core patterns in vanilla JS
 * Appended to existing ziwei.js
 */
(function(){
  if (!ZW || typeof ZW !== 'object') return;

  // ── Constants ──
  var SHA_NAMES = ['擎羊','陀罗','火星','铃星','地空','地劫'];
  var SHA_HARD = ['擎羊','陀罗','火星','铃星'];

  // ── Helpers ──
  function getStarsByType(palace, type) {
    return palace.stars.filter(function(s) { return s.type === type; });
  }
  function hasStar(palace, name) {
    return palace.stars.some(function(s) { return s.name === name; });
  }
  function getPalaceByBranch(chart, branch) {
    return chart.palaces.find(function(p) { return p.branch === ((branch%12)+12)%12; });
  }
  function getSanFangSet(chart) {
    var m = chart.mingBranch;
    var branches = [m, (m+4)%12, (m+8)%12, (m+6)%12];
    var names = {};
    chart.palaces.filter(function(p) { return branches.indexOf(p.branch)>=0; })
      .forEach(function(p) { p.stars.forEach(function(s) { names[s.name]=true; }); });
    return Object.keys(names);
  }
  function shaCountInPalace(palace, list) {
    list = list || SHA_HARD;
    return palace.stars.filter(function(s) { return list.indexOf(s.name)>=0; }).length;
  }
  function sanFangShaCount(chart, list) {
    var m = chart.mingBranch;
    var branches = [m, (m+4)%12, (m+8)%12, (m+6)%12];
    var count = 0;
    chart.palaces.filter(function(p) { return branches.indexOf(p.branch)>=0; })
      .forEach(function(p) { count += shaCountInPalace(p, list); });
    return count;
  }

  // ═══════════ PATTERN DETECTION ═══════════

  /** 紫府同宫: 紫微+天府 in ming */
  function detectZiFu(chart, ming, allMajors) {
    if (allMajors.indexOf('紫微')>=0 && allMajors.indexOf('天府')>=0) {
      return {name:'紫府同宫',level:'excellent',
        desc:'紫微天府同入命宫，帝相并临，尊贵之命。主品行端正、衣食无忧、有领导才能，宜担任要职。古书云"紫府同宫，富贵双全"。',
        source:'《紫微斗数全书·紫府同宫格》'};
    }
    return null;
  }

  /** 日月并明: 太阳+太阴 in ming */
  function detectRiYueBingMing(chart, ming, allMajors) {
    if (allMajors.indexOf('太阳')>=0 && allMajors.indexOf('太阴')>=0) {
      return {name:'日月并明',level:'excellent',
        desc:'太阳太阴同入命宫，阴阳调和，文武兼备。主异性缘佳、事业顺遂、名声远播。古书云"日月同宫，贵不可言"。',
        source:'《紫微斗数全书·日月同宫》'};
    }
    return null;
  }

  /** 君臣庆会: 紫微入命 + 左辅右弼在三方 */
  function detectJunChen(chart, ming, allMajors) {
    if (allMajors.indexOf('紫微')<0) return null;
    var sf = getSanFangSet(chart);
    if (sf.indexOf('左辅')>=0 && sf.indexOf('右弼')>=0) {
      return {name:'君臣庆会',level:'excellent',
        desc:'紫微入命，左辅右弼同会，帝王得贤臣辅佐。主大富大贵、统御之命。一生贵人不绝，宜走政商高位、跨界领袖之途。',
        source:'《紫微斗数全书·君臣庆会格》'};
    }
    return null;
  }

  /** 七杀朝斗: 七杀独坐命宫 */
  function detectQiSha(chart, ming, allMajors) {
    if (allMajors.length===1 && allMajors[0]==='七杀') {
      return {name:'七杀朝斗',level:'good',
        desc:'七杀独坐命宫，将星入命。性格刚烈果决，不畏艰难。宜军警、外科医生、创业者。需防孤克之性，晚婚为宜，中年后方显英雄本色。',
        source:'《紫微斗数全书·七杀》'};
    }
    return null;
  }

  /** 杀破狼: 七杀+破军+贪狼三方齐聚 */
  function detectShaPoLang(chart, ming, allMajors) {
    var sf = getSanFangSet(chart);
    var has3 = ['七杀','破军','贪狼'].filter(function(s) { return sf.indexOf(s)>=0; });
    if (has3.length >= 3) {
      return {name:'杀破狼',level:'good',
        desc:'七杀、破军、贪狼三星会命，开创闯荡之命格。一生变动多、不甘平凡，宜创业、军警、业务、销售。中年后才能稳定守成，年轻时易因冲动失利。',
        source:'《紫微斗数全书·杀破狼》'};
    }
    return null;
  }

  /** 机月同梁: 天机+太阴+天同+天梁 */
  function detectJiYue(chart, ming, allMajors) {
    var sf = getSanFangSet(chart);
    var has4 = ['天机','太阴','天同','天梁'].filter(function(s) { return sf.indexOf(s)>=0; });
    if (has4.length >= 4) {
      return {name:'机月同梁',level:'excellent',
        desc:'天机太阴天同天梁四星齐入命迁财官，文质彬彬、聪慧善谋。最适合公职、学术、文艺、医疗、服务等需稳定累积的行业，不宜大冒险大投机。',
        source:'《紫微斗数全书·机月同梁格》'};
    }
    return null;
  }

  /** 武贪格: 武曲+贪狼同宫或对照 */
  function detectWuTan(chart, ming, allMajors) {
    if (allMajors.indexOf('武曲')>=0 && allMajors.indexOf('贪狼')>=0) {
      return {name:'武贪格',level:'excellent',
        desc:'武曲贪狼同入命宫，财星与桃花星交辉。古书云"武贪不发少年人"——三十岁后方能厚积薄发。主中年以后大富大贵，适合金融、投机、娱乐业。',
        source:'《紫微斗数骨髓赋》'};
    }
    return null;
  }

  /** 火贪格/铃贪格: 贪狼+火/铃 */
  function detectHuoLingTan(chart, ming, allMajors) {
    var sf = getSanFangSet(chart);
    if (allMajors.indexOf('贪狼')>=0) {
      if (sf.indexOf('火星')>=0) return {name:'火贪格',level:'excellent',
        desc:'贪狼遇火星会照，主突发横财、突如其来的机遇。古书云"贪狼遇火铃，必发横财"，但来得快去得也快，宜见好就收。',
        source:'《紫微斗数骨髓赋》'};
      if (sf.indexOf('铃星')>=0) return {name:'铃贪格',level:'excellent',
        desc:'贪狼遇铃星会照，横发之机。但铃星为暗曜，财来较隐晦，需谨慎投资，见好即收。',
        source:'《紫微斗数骨髓赋》'};
    }
    return null;
  }

  /** 阳梁昌禄: 太阳+天梁+文昌+禄存 */
  function detectYangLiang(chart, ming, allMajors) {
    var sf = getSanFangSet(chart);
    if (sf.indexOf('太阳')>=0 && sf.indexOf('天梁')>=0 && sf.indexOf('文昌')>=0 && sf.indexOf('禄存')>=0) {
      return {name:'阳梁昌禄',level:'excellent',
        desc:'太阳、天梁、文昌、禄存四星齐会命宫三方，号"科举之星"。主清贵显达、考运极佳，宜走学术、文教、研究、专业认证之路，一生功名易就。',
        source:'《紫微斗数全书·阳梁昌禄格》'};
    }
    return null;
  }

  /** 巨日同宫: 巨门+太阳 in ming */
  function detectJuRi(chart, ming, allMajors) {
    if (allMajors.indexOf('巨门')>=0 && allMajors.indexOf('太阳')>=0) {
      return {name:'巨日同宫',level:'good',
        desc:'巨门太阳同入命宫，太阳化解巨门暗曜。主以口才、传媒、外语、专业立业。化禄化权则口才生财，化忌则需防口舌官非。',
        source:'《紫微斗数全书·巨日同宫》'};
    }
    return null;
  }

  /** 武曲七杀: 武曲+七杀 in ming */
  function detectWuQi(chart, ming, allMajors) {
    if (allMajors.indexOf('武曲')>=0 && allMajors.indexOf('七杀')>=0) {
      return {name:'武曲七杀',level:'good',
        desc:'武曲七杀同入命宫，将星配财星。主果决刚毅、理财能力强，适合金融、军警、创业。一生奋斗、积财但操心。化禄化权则发达，化忌则需防财劫。',
        source:'《紫微斗数全书》'};
    }
    return null;
  }

  /** 天同天梁: 天同+天梁 in ming */
  function detectTongLiang(chart, ming, allMajors) {
    if (allMajors.indexOf('天同')>=0 && allMajors.indexOf('天梁')>=0) {
      return {name:'天同天梁格',level:'good',
        desc:'天同天梁同入命宫，福星与荫星共会。主宽厚和善、乐于助人，宜医疗、教育、宗教、社会公益。但偏温和保守，难成大富大贵之局。',
        source:'《紫微斗数全书》'};
    }
    return null;
  }

  /** 石中隐玉: 巨门独坐命宫(子/午) */
  function detectShiZhong(chart, ming) {
    var majors = getStarsByType(ming,'major');
    if (majors.length===1 && majors[0].name==='巨门' && (ming.branch===0||ming.branch===6)) {
      return {name:'石中隐玉',level:'excellent',
        desc:'巨门坐命子午，外表平凡而内蕴才学。早年默默无闻、中年方显贵气，宜走专业、研究、口才、传媒。需有禄权或文昌相助方能"凿石见玉"。',
        source:'《紫微斗数骨髓赋·石中隐玉》'};
    }
    return null;
  }

  /** 明珠出海: 命宫在未空宫，对宫丑为日月 */
  function detectMingZhu(chart, ming) {
    if (ming.branch!==7) return null;
    if (getStarsByType(ming,'major').length>0) return null;
    var dui = getPalaceByBranch(chart, (ming.branch+6)%12);
    if (!dui) return null;
    if (hasStar(dui,'太阳') && hasStar(dui,'太阴')) {
      return {name:'明珠出海',level:'excellent',
        desc:'命未空宫，对宫丑宫日月同辉拱照，号"明珠出海"。主出生平凡、后天努力出头，宜远赴他乡、学术研究或大公司高位，主大富大贵。',
        source:'《紫微斗数全集·明珠出海》'};
    }
    return null;
  }

  /** 紫微入命（独坐）*/
  function detectZiWeiInMing(chart, ming, allMajors) {
    if (allMajors.indexOf('紫微')>=0 && allMajors.indexOf('天府')<0) {
      var sf = getSanFangSet(chart);
      if (sf.indexOf('左辅')>=0 || sf.indexOf('右弼')>=0) {
        return {name:'紫微入命',level:'good',
          desc:'紫微独坐命宫，帝王之星。自尊心强、有领导魅力。得辅弼相助则贵气加身，无辅弼则为"孤君"需自省。一生宜走管理、高级专业路线。',
          source:'《紫微斗数全书》'};
      }
    }
    return null;
  }

  // ═══════════ MAIN detectPatterns ═══════════
  ZW.detectPatterns = function(chart) {
    var patterns = [];
    var ming = chart.palaces.find(function(p) { return p.isMing; });
    if (!ming) return patterns;
    var allMajors = getStarsByType(ming,'major').map(function(s) { return s.name; });
    
    var detectors = [
      detectZiFu, detectRiYueBingMing, detectJunChen, detectQiSha,
      detectShaPoLang, detectJiYue, detectWuTan, detectHuoLingTan,
      detectYangLiang, detectJuRi, detectWuQi, detectTongLiang,
      detectShiZhong, detectMingZhu, detectZiWeiInMing
    ];
    
    detectors.forEach(function(fn) {
      var result = fn(chart, ming, allMajors);
      if (result) {
        patterns.push({
          name: result.name,
          level: result.level,
          desc: result.desc,
          source: result.source
        });
      }
    });
    
    return patterns;
  };

})();
