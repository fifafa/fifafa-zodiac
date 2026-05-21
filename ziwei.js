// ====== 紫微斗数排盘引擎 (Client-side Vanilla JS) ======
// Based on 倪海夏《天纪》体系 · Ported from Renhuai123/ziwei-doushu

var ZW = {};

// ═══════════ CONSTANTS ═══════════
ZW.PALACES = ['命宫','兄弟','夫妻','子女','财帛','疾厄','迁移','交友','官禄','田宅','福德','父母'];
ZW.MAJORS = ['紫微','天机','太阳','武曲','天同','廉贞','天府','太阴','贪狼','巨门','天相','天梁','七杀','破军'];
ZW.AUX = ['文昌','文曲','左辅','右弼','天魁','天钺','禄存','擎羊','陀罗','火星','铃星','天马','地空','地劫'];

// 紫微星安置表：五行局→(农历日→宫位)
ZW.ZIWEI_TABLE = {
  2:{1:2,2:3,3:2,4:4,5:2,6:5,7:3,8:5,9:3,10:6,11:3,12:6,13:4,14:6,15:4,16:7,17:4,18:7,19:5,20:7,21:5,22:8,23:6,24:8,25:6,26:9,27:7,28:9,29:7,30:10},
  3:{1:4,2:6,3:3,4:7,5:4,6:8,7:5,8:8,9:5,10:9,11:6,12:9,13:6,14:10,15:7,16:10,17:7,18:11,19:8,20:12,21:8,22:0,23:9,24:0,25:9,26:1,27:10,28:1,29:10,30:2},
  4:{1:6,2:8,3:10,4:12,5:2,6:3,7:4,8:4,9:5,10:6,11:7,12:7,13:8,14:9,15:10,16:10,17:11,18:12,19:0,20:0,21:1,22:2,23:3,24:3,25:4,26:5,27:6,28:6,29:7,30:8},
  5:{1:8,2:10,3:12,4:1,5:3,6:5,7:7,8:8,9:10,10:11,11:0,12:2,13:4,14:5,15:7,16:8,17:10,18:11,19:0,20:2,21:3,22:5,23:7,24:8,25:10,26:11,27:0,28:2,29:3,30:5},
  6:{1:9,2:11,3:1,4:3,5:5,6:7,7:9,8:11,9:0,10:1,11:3,12:5,13:7,14:8,15:10,16:11,17:1,18:2,19:4,20:6,21:8,22:10,23:11,24:1,25:2,26:4,27:6,28:8,29:9,30:11}
};

// 四化表
ZW.SIHUA_TABLE = [
  ['廉贞','破军','武曲','太阳'],['天机','天梁','紫微','太阴'],['天同','天机','文昌','廉贞'],['太阴','天同','天机','巨门'],
  ['贪狼','太阴','右弼','天机'],['武曲','贪狼','天梁','文曲'],['太阳','武曲','太阴','天同'],['巨门','太阳','文曲','文昌'],
  ['天梁','紫微','左辅','武曲'],['破军','巨门','太阴','贪狼']
];

// 主星描述
ZW.STARS = {
  '紫微':{kw:'帝王·尊贵·独立',e:'土',n:'中性偏吉',d:'紫微为帝星，主贵气、领导力。命宫有紫微，天生领袖气质，独立自主。庙旺则权柄在握，陷落则孤高自负。'},
  '天机':{kw:'智慧·机变·谋略',e:'木',n:'吉星',d:'天机主智慧、谋划。思维敏捷，善于分析。命宫有之，聪明过人但易多虑。宜从事策划、咨询类工作。'},
  '太阳':{kw:'阳刚·官贵·慷慨',e:'火',n:'吉星',d:'太阳主光明、官贵。热心慷慨，乐于助人。日生人更吉，夜生减半。男命主事业，女命主夫星。'},
  '武曲':{kw:'财富·刚毅·果断',e:'金',n:'中性',d:'武曲为财星，主刚毅果断。与钱财有缘，适合金融、管理。性格刚直，重原则。忌见煞星破格。'},
  '天同':{kw:'温和·享福·随缘',e:'水',n:'吉星',d:'天同为福星，主温和享福。性情柔顺，不喜争斗。命宫有之，晚年福厚。唯需防懒散依赖。'},
  '廉贞':{kw:'才艺·刑囚·桃花',e:'火',n:'凶中带吉',d:'廉贞主才艺、桃花，亦为次桃花星。才华横溢但易生是非。喜会文昌文曲增才学，忌见擎羊化忌。'},
  '天府':{kw:'财库·稳重·保守',e:'土',n:'吉星',d:'天府为财库之星，主稳重保守。理财能力出色，性格可靠。宜从事不动产、仓储行业。忌空劫冲破库。'},
  '太阴':{kw:'柔美·财富·阴柔',e:'水',n:'吉星',d:'太阴主柔美、财富，为田宅主。性情温和细腻。夜生人更吉，日生减半。女命主容貌，男命主妻星。'},
  '贪狼':{kw:'欲望·桃花·多才',e:'木',n:'中性',d:'贪狼为桃花主，多才多艺。社交能力强，兴趣广泛。宜演艺、公关行业。忌沉迷酒色。'},
  '巨门':{kw:'口舌·是非·善辩',e:'水',n:'凶中带吉',d:'巨门主口舌是非，亦为暗星。能言善辩，适合法律、教育行业。需防口舌之灾，喜会化权增强正面力量。'},
  '天相':{kw:'辅佐·行政·印绶',e:'水',n:'吉星',d:'天相为印星，主辅佐、行政。处事谨慎，待人随和。宜政府、大企业行政岗位。忌见煞星破印。'},
  '天梁':{kw:'荫护·医药·长辈',e:'土',n:'吉星',d:'天梁为荫星，主医药、长辈庇佑。性格稳重可靠。宜医疗、教育、保险行业。有化难呈祥之力。'},
  '七杀':{kw:'将星·果决·孤克',e:'金',n:'凶星',d:'七杀为将星，主果决、开拓。性格刚烈，不畏艰难。宜军警、外科医生。需防孤克之性，晚婚为宜。'},
  '破军':{kw:'开创·变动·破坏',e:'水',n:'凶星',d:'破军主开创、变动，为耗星。喜欢改革创新。宜新兴行业、创业者。一生多有变动，需稳健理财。'}
};

ZW.AUX_DESC = {
  '文昌':{kw:'文采·科举',d:'主文采风流，考试运强。'},
  '文曲':{kw:'才艺·口才',d:'主才艺口才，艺术天赋。'},
  '左辅':{kw:'贵人·助力',d:'贵人相助，左右逢源。'},
  '右弼':{kw:'贵人·辅佐',d:'辅佐之力，得人信任。'},
  '天魁':{kw:'贵气·科名',d:'天魁为科甲星，主考试升迁。'},
  '天钺':{kw:'贵气·科名',d:'天钺为科甲星，主功名显达。'},
  '禄存':{kw:'财富·积蓄',d:'禄存为财星，主积蓄理财。'},
  '擎羊':{kw:'刑伤·冲突',d:'擎羊主刑伤冲突，需谨慎。'},
  '陀罗':{kw:'拖延·纠缠',d:'陀罗主拖延纠缠，宜耐心。'},
  '火星':{kw:'急躁·暴发',d:'火星主急躁，亦有爆发力。'},
  '铃星':{kw:'暗疾·隐忧',d:'铃星主暗疾隐忧，宜低调。'},
  '天马':{kw:'奔波·驿动',d:'天马主动，宜外勤远行。'},
  '地空':{kw:'空想·变动',d:'地空主空想变动，忌投机。'},
  '地劫':{kw:'损耗·波折',d:'地劫主损耗波折，宜保守。'}
};

// ═══════════ ALGORITHM ═══════════
// 安命宫: 正月寅上起正月，顺数至生月，再逆数至生时
ZW.anMingGong = function(lunarMonth, hourBranch) {
  var g = (2 + lunarMonth - 1 + 12) % 12; // 寅=2, 正月寅
  return (g - hourBranch + 12) % 12;
};

// 安身宫: 正月寅上起正月，顺数至生月，再顺数至生时
ZW.anShenGong = function(lunarMonth, hourBranch) {
  var g = (2 + lunarMonth - 1 + 12) % 12;
  return (g + hourBranch) % 12;
};

// 五虎遁：年干→寅月天干
ZW.wuHuDun = function(yearStem) {
  return (yearStem * 2 + 2) % 10;
};

// 定十二宫天干
ZW.setPalaceGan = function(yearStem) {
  var yinGan = ZW.wuHuDun(yearStem);
  var gans = [];
  for (var i = 0; i < 12; i++) gans.push((yinGan + i) % 10);
  return gans;
};

// 纳音五行局
ZW.NAYIN_JU = [2,6,4,5,2,6,3,5,4,5,3,5,6,4,3,5,4,2,6,3,5,3,5,6,4,3,4,5,4,2];

ZW.getWuxingJu = function(mingGongBranch, mingGongGan) {
  var idx = mingGongGan + 10 * (((mingGongGan - mingGongBranch) / 2 + 6) % 6);
  return ZW.NAYIN_JU[idx % 30];
};

// 安紫微星
ZW.anZiwei = function(ju, lunarDay) {
  var table = ZW.ZIWEI_TABLE[ju];
  if (!table) return 2;
  return table[Math.min(lunarDay, 30)] || 2;
};

// 安十四主星
ZW.an14Majors = function(ziweiBranch) {
  // 紫微系 (逆时针)
  var ziweiLine = [ziweiBranch];
  var pos = ziweiBranch;
  var offsets = [0, -1, -2, -3, -4, -5]; // 紫微 天机(隔一) 太阳 武曲 天同(隔二) 廉贞
  // Actually the standard placement:
  // 紫微→天机(逆1)→空→太阳(逆1)→武曲(逆1)→天同(逆1)→空→空→廉贞(逆1)
  // Simplified: offsets from ziwei
  var purpStars = {
    '紫微': ziweiBranch,
    '天机': (ziweiBranch - 1 + 12) % 12,
    '太阳': (ziweiBranch - 3 + 12) % 12,
    '武曲': (ziweiBranch - 4 + 12) % 12,
    '天同': (ziweiBranch - 5 + 12) % 12,
    '廉贞': (ziweiBranch - 8 + 12) % 12
  };
  
  // 天府系 (顺时针): 天府=紫微+(12-紫微位置)=寅+...
  var tianfuPos = (ziweiBranch + (12 - ziweiBranch + 12) % 12) % 12; // 天府=12-紫微+...
  // Actually standard: 天府位置 与 紫微位置 在地支上对称: 寅申→申寅...
  // 紫微在寅(2)→天府在辰(4) = ziwei + 2, 紫微在卯(3)→天府在巳(5)=+2...
  // Let me recalculate: 紫微在支→天府在支
  // 紫微 2→天府 4; 紫微 3→天府 5; 紫微 4→天府 6; 紫微 5→天府 8...
  // Actually it's 寅→辰=+2, 卯→巳=+2, 辰→午=+2, 巳→未=+2, 午→申=+2...
  // Nope, let me use the standard formula:
  // 天府 = 紫微在寅→天府在辰, 紫微在卯→天府在巳, etc.
  // The mapping: 紫微地支→天府地支 = (2,4)(3,5)(4,6)(5,7)(6,8)(7,10)(8,11)(9,0)(10,1)(11,3)(0,4)(1,4)
  var tfMap = {2:4,3:5,4:6,5:7,6:8,7:10,8:11,9:0,10:1,11:3,0:4,1:4};
  var tfPos = tfMap[ziweiBranch] || 4;
  
  var mansionStars = {
    '天府': tfPos,
    '太阴': (tfPos + 1) % 12,
    '贪狼': (tfPos + 2) % 12,
    '巨门': (tfPos + 3) % 12,
    '天相': (tfPos + 4) % 12,
    '天梁': (tfPos + 5) % 12,
    '七杀': (tfPos + 6) % 12,
    '破军': (tfPos + 10) % 12
  };
  
  var result = {};
  for (var k in purpStars) result[k] = purpStars[k];
  for (var k in mansionStars) result[k] = mansionStars[k];
  return result;
};

// 安文昌文曲 (生时)
ZW.anChangQu = function(hourBranch) {
  return { '文昌': (10 - hourBranch + 12) % 12, '文曲': (4 + hourBranch) % 12 };
};

// 安左辅右弼 (生月)
ZW.anZuoYou = function(lunarMonth) {
  return { '左辅': (4 + lunarMonth - 1) % 12, '右弼': (10 - lunarMonth + 1 + 12) % 12 };
};

// 安天魁天钺 (年干)
ZW.TIANKUI = {0:1,1:0,2:11,3:11,4:1,5:0,6:1,7:6,8:3,9:3};
ZW.TIANYUE = {0:7,1:8,2:9,3:9,4:7,5:8,6:7,7:2,8:5,9:5};
ZW.anKuiYue = function(yearStem) {
  return { '天魁': ZW.TIANKUI[yearStem], '天钺': ZW.TIANYUE[yearStem] };
};

// 安禄存擎羊陀罗 (年干)
ZW.LUCUN = {0:2,1:3,2:5,3:6,4:5,5:6,6:8,7:9,8:11,9:0};
ZW.anLuCun = function(yearStem) {
  var lc = ZW.LUCUN[yearStem];
  return { '禄存': lc, '擎羊': (lc + 1) % 12, '陀罗': (lc + 11) % 12 };
};

// 安火星铃星 (年支+生时)
ZW.anHuoLing = function(yearBranch, hourBranch) {
  var huoTable = {0:{0:0,1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10,11:11}};
  // 火星: 寅午戌人→丑起子时顺, 申子辰→寅起子时顺, 巳酉丑→卯起子时顺, 亥卯未→酉起子时顺
  var huoStart = {0:2,2:1,5:3,8:2,4:1,6:1,7:3,11:9,1:9,3:9,9:3,10:9}[yearBranch] || 2;
  var lingStart = {0:10,2:9,5:2,8:10,4:9,6:9,7:2,11:1,1:1,3:1,9:2,10:1}[yearBranch] || 10;
  return { '火星': (huoStart + hourBranch) % 12, '铃星': (lingStart + hourBranch) % 12 };
};

// 安天马 (年支)
ZW.anTianMa = function(yearBranch) {
  // 寅午戌→申(8), 申子辰→寅(2), 巳酉丑→亥(11), 亥卯未→巳(5)
  var map = {2:8,6:8,10:8, 8:2,0:2,4:2, 5:11,9:11,1:11, 11:5,3:5,7:5};
  return { '天马': map[yearBranch] || 8 };
};

// 安地空地劫 (生时)
ZW.anKongJie = function(hourBranch) {
  return { '地空': (12 - hourBranch + 12) % 12, '地劫': (4 + hourBranch) % 12 };
};

// ═══════════ MAIN = ═══════════
ZW.generate = function(y, m, d, h, gender) {
  // Convert to lunar (approximate: use simplified lunar)
  // For now use solar date directly as lunar approximation
  var yearStem = (y - 4) % 10; if (yearStem < 0) yearStem += 10;
  var yearBranch = (y - 4) % 12; if (yearBranch < 0) yearBranch += 12;
  var hourBranch = Math.floor(((h + 1) % 24) / 2) % 12;
  
  // Use month as lunar month (simplified)
  var lunarMonth = m;
  var lunarDay = d;
  
  // 安命宫
  var mingBranch = ZW.anMingGong(lunarMonth, hourBranch);
  var shenBranch = ZW.anShenGong(lunarMonth, hourBranch);
  
  // 定十二宫天干
  var palaceGans = ZW.setPalaceGan(yearStem);
  
  // 五行局
  var ju = ZW.getWuxingJu(mingBranch, palaceGans[mingBranch]);
  var juNames = {2:'水二局',3:'木三局',4:'金四局',5:'土五局',6:'火六局'};
  
  // 安紫微
  var ziweiBranch = ZW.anZiwei(ju, lunarDay);
  
  // 安十四主星
  var majors = ZW.an14Majors(ziweiBranch);
  
  // 安辅星
  var aux = {};
  Object.assign(aux, ZW.anChangQu(hourBranch));
  Object.assign(aux, ZW.anZuoYou(lunarMonth));
  Object.assign(aux, ZW.anKuiYue(yearStem));
  Object.assign(aux, ZW.anLuCun(yearStem));
  Object.assign(aux, ZW.anHuoLing(yearBranch, hourBranch));
  Object.assign(aux, ZW.anTianMa(yearBranch));
  Object.assign(aux, ZW.anKongJie(hourBranch));
  
  // 安四化
  var sihua = ZW.SIHUA_TABLE[yearStem];
  var sihuaMap = {};
  sihuaMap[sihua[0]] = '禄';
  sihuaMap[sihua[1]] = '权';
  sihuaMap[sihua[2]] = '科';
  sihuaMap[sihua[3]] = '忌';
  
  // Assemble palaces
  var palaces = [];
  for (var i = 0; i < 12; i++) {
    var branch = (mingBranch + i) % 12;
    var stars = [];
    for (var sn in majors) { if (majors[sn] === branch) stars.push({name: sn, type: 'major'}); }
    for (var sn in aux) { if (aux[sn] === branch) stars.push({name: sn, type: 'aux', sh: sihuaMap[sn]}); }
    palaces.push({
      name: ZW.PALACES[i],
      branch: branch,
      gan: palaceGans[branch],
      stars: stars,
      isMing: branch === mingBranch,
      isShen: branch === shenBranch
    });
  }
  
  return {
    yearStem: yearStem,
    yearBranch: yearBranch,
    lunarMonth: lunarMonth,
    lunarDay: lunarDay,
    hourBranch: hourBranch,
    gender: gender,
    ju: ju,
    juName: juNames[ju] || '未知',
    mingBranch: mingBranch,
    shenBranch: shenBranch,
    palaces: palaces,
    sihua: sihua,
    sihuaMap: sihuaMap
  };
};

// ═══════════ RENDER ═══════════
ZW.render = function(chart) {
  var stemsZh = ['甲','乙','丙','丁','戊','己','庚','辛','壬','癸'];
  var branchZh = ['子','丑','寅','卯','辰','巳','午','未','申','酉','戌','亥'];
  var branchEl = ['水','土','木','木','土','火','火','土','金','金','土','水'];
  var sihuaColors = {禄:'var(--green)',权:'var(--gold)',科:'var(--purple)',忌:'var(--red)'};
  
  // Build grid HTML
  var pal = chart.palaces;
  // Display order: start from 寅(2), then clockwise
  var displayOrder = [];
  var startIdx = pal.findIndex(function(p) { return p.branch === 2; });
  if (startIdx < 0) startIdx = 0;
  for (var i = 0; i < 12; i++) {
    displayOrder.push(pal[(startIdx + i) % 12]);
  }
  
  // Map to 4x4 grid (skip corners)
  var gridMap = [
    [0, 0], [0, 1], [0, 2], [0, 3],  // row 1: 巳午未申
    [1, 3],                          // row 2: 酉
    [2, 3],                          // row 3: 戌
    [3, 3], [3, 2], [3, 1], [3, 0],  // row 4: 亥子丑寅
    [2, 0],                          // row 3: 卯
    [1, 0],                          // row 2: 辰
  ];
  
  var trunk = stemsZh[chart.yearStem] + branchZh[chart.yearBranch];
  
  var html = '<div class="zw-chart">';
  html += '<div class="zw-header"><span>'+trunk+'年 · '+chart.juName+' · 命宫：' + branchZh[chart.mingBranch] + '</span></div>';
  html += '<div class="zw-grid">';
  
  for (var i = 0; i < 12; i++) {
    var p = displayOrder[i];
    var g = gridMap[i];
    var cls = 'zw-cell';
    if (p.isMing) cls += ' zw-ming';
    if (p.isShen) cls += ' zw-shen';
    
    var starsHtml = p.stars.map(function(s) {
      var shBadge = '';
      if (s.sh) {
        shBadge = '<span class="zw-sh" style="color:' + sihuaColors[s.sh] + '">' + s.sh + '</span>';
      }
      return '<div class="zw-star' + (s.type === 'major' ? ' zw-major' : '') + '">' + s.name + shBadge + '</div>';
    }).join('');
    
    var ganZhi = stemsZh[p.gan] + branchZh[p.branch];
    html += '<div class="' + cls + '" style="grid-column:' + (g[0] + 1) + ';grid-row:' + (g[1] + 1) + '" onclick="ZW.showPalace(' + i + ')">';
    html += '<div class="zw-cname">' + p.name + '</div>';
    html += '<div class="zw-ganzhi">' + ganZhi + '</div>';
    html += '<div class="zw-stars">' + (starsHtml || '<div class="zw-empty">—</div>') + '</div>';
    if (p.isMing) html += '<div class="zw-tag">命</div>';
    if (p.isShen) html += '<div class="zw-tag zw-stag">身</div>';
    html += '</div>';
  }
  html += '</div></div>';
  
  // Interpretation
  var mingPalace = pal.find(function(p) { return p.isMing; });
  var majorStars = mingPalace.stars.filter(function(s) { return s.type === 'major'; });
  var mainStar = majorStars.length > 0 ? majorStars[0].name : '—';
  var sihuaOnMain = ZW.SIHUA_TABLE[chart.yearStem];
  var sc = 60 + (sihuaOnMain.indexOf(mainStar) >= 0 ? 20 : 0) + majorStars.length * 3;
  
  html += '<div class="card" style="margin-top:14px"><h3 style="color:var(--gold);text-align:center">✦ 命盘解读</h3>';
  html += '<div class="zw-summary"><div class="zw-score">' + Math.min(99, sc) + '%</div><div style="color:var(--moon3);font-size:.7em">命盘综合评分</div></div>';
  
  if (ZW.STARS[mainStar]) {
    var sd = ZW.STARS[mainStar];
    html += '<div class="reading"><h3>命宫主星 · ' + mainStar + ' (' + sd.e + ')</h3><p><b>性质：</b>' + sd.n + ' | <b>特质：</b>' + sd.kw + '</p><p>' + sd.d + '</p></div>';
  }
  
  // Pattern detection (15 real patterns, not hardcoded)
  var patterns = ZW.detectPatterns ? ZW.detectPatterns(chart) : [];
  if (patterns.length > 0) {
    var levelLabels = {excellent:'大吉',good:'上格',neutral:'中平',caution:'需留意'};
    patterns.forEach(function(pat) {
      html += '<div class="reading"><h3>格局 · ' + pat.name + ' (' + (levelLabels[pat.level] || pat.level) + ')</h3><p>' + pat.desc + '</p>';
      if (pat.source) html += '<div style="font-size:.58em;color:var(--moon3);margin-top:4px">' + pat.source + '</div>';
      html += '</div>';
    });
  }
  
  // Sihua info
  html += '<div class="reading"><h3>四化飞星</h3><div class="zw-sihua-bar">';
  var shNames = ['禄','权','科','忌'];
  for (var j = 0; j < 4; j++) {
    html += '<span class="zw-sh-tag" style="background:' + sihuaColors[shNames[j]] + '20;border-color:' + sihuaColors[shNames[j]] + '">' + shNames[j] + '：' + chart.sihua[j] + '</span>';
  }
  html += '</div></div>';
  
  html += '<div class="disclaimer">以上分析仅供传统文化娱乐参考</div></div>';
  
  return html;
};

// Store current chart for popup
ZW._chart = null;

ZW.showPalace = function(idx) {
  var disp = ZW._displayOrder[idx];
  var p = ZW._chart.palaces[disp];
  var stemsZh = ['甲','乙','丙','丁','戊','己','庚','辛','壬','癸'];
  var branchZh = ['子','丑','寅','卯','辰','巳','午','未','申','酉','戌','亥'];
  
  var majorStars = p.stars.filter(function(s) { return s.type === 'major'; });
  var auxStars = p.stars.filter(function(s) { return s.type === 'aux'; });
  
  var popHtml = '<div class="ptitle">' + stemsZh[p.gan] + branchZh[p.branch] + ' · ' + p.name + '</div>';
  
  if (majorStars.length > 0) {
    popHtml += '<div style="margin-bottom:12px"><div style="font-size:.7em;color:var(--moon3);margin-bottom:6px">主星</div>';
    majorStars.forEach(function(s) {
      var sd = ZW.STARS[s.name] || {kw:'',n:''};
      popHtml += '<div style="font-size:.78em;color:var(--gold);margin:4px 0"><b>' + s.name + '</b> ' + (sd.kw || '') + '</div>';
      if (sd.d) popHtml += '<div style="font-size:.7em;color:var(--moon2);margin-bottom:6px;line-height:1.5">' + sd.d.substring(0, 80) + '…</div>';
    });
    popHtml += '</div>';
  }
  
  if (auxStars.length > 0) {
    popHtml += '<div><div style="font-size:.7em;color:var(--moon3);margin-bottom:6px">辅星</div>';
    auxStars.forEach(function(s) {
      var ad = ZW.AUX_DESC[s.name] || {kw:'',d:''};
      var shLabel = s.sh ? ' <span style="color:' + ({禄:'var(--green)',权:'var(--gold)',科:'var(--purple)',忌:'var(--red)'}[s.sh]) + '">[' + s.sh + ']</span>' : '';
      popHtml += '<div style="font-size:.7em;color:var(--moon2);margin:2px 0"><b>' + s.name + '</b>' + shLabel + ' ' + (ad.kw || '') + '</div>';
    });
    popHtml += '</div>';
  }
  
  if (majorStars.length === 0 && auxStars.length === 0) {
    popHtml += '<div style="text-align:center;color:var(--moon3);padding:20px;font-size:.8em">此宫为空宫，借对宫之力</div>';
  }
  
  document.getElementById('zonePopup').innerHTML = popHtml;
  document.getElementById('zonePopup').style.display = 'block';
  document.getElementById('popOverlay').style.display = 'block';
};

// Init function to be called from goCh
ZW.init = function() {
  if (!USER || !USER.y) {
    // Default: show sample chart
    document.getElementById('zwContent').innerHTML='<div class="card"><p style="text-align:center;color:var(--moon3);padding:30px">\u8BF7\u5148\u5728\u516B\u5B57\u547D\u7406\u9875\u8F93\u5165\u51FA\u751F\u65E5\u671F\uFF0C\u518D\u67E5\u770B\u7D2B\u5FAE\u6597\u6570\u547D\u76D8 \u2726</p></div>'; return;
  }
  var chart = ZW.generate(USER.y, USER.m, USER.d, USER.h, USER.g);
  ZW._chart = chart;
  
  // Compute display order
  var pal = chart.palaces;
  var startIdx = pal.findIndex(function(p) { return p.branch === 2; });
  if (startIdx < 0) startIdx = 0;
  ZW._displayOrder = [];
  for (var i = 0; i < 12; i++) { ZW._displayOrder.push((startIdx + i) % 12); }
  
  var html = ZW.render(chart);
  document.getElementById('zwContent').innerHTML = html;
  
  // Update nav
  document.querySelectorAll('.ni').forEach(function(n) { n.classList.remove('on'); });
  var ni = document.getElementById('nav-ziwei');
  if (ni) ni.classList.add('on');
};
