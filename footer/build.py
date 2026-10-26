#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把 footer.html 组装成三种形态，生成 index.html（设计交付页）。

    python3 build.py

改完 footer.html / footer.css 后重跑一次即可，避免三处手改走样。
"""
from pathlib import Path

base = Path(__file__).parent
full = (base / "footer.html").read_text(encoding="utf-8")

light = full.replace('<footer class="plnl-footer">', '<footer class="plnl-footer plnl-footer--light">')
compact = full.replace('<footer class="plnl-footer">', '<footer class="plnl-footer plnl-footer--compact">')

# 紧凑版：一行结构，单独写死（比正则抠更稳）
compact = """<footer class="plnl-footer plnl-footer--compact">
  <div class="plnl-footer__compact-row">
    <a class="plnl-brand" href="https://plnl.vip" aria-label="PLNL 本德 · 返回首页">
      <span class="plnl-brand__mark" aria-hidden="true">
        <svg viewBox="0 0 24 24" fill="none">
          <path d="M3 17.5 9 9.5l3.4 4.6L15 11l6 6.5" stroke="#08202f" stroke-width="1.8"
                stroke-linecap="round" stroke-linejoin="round"/>
          <circle cx="8.2" cy="6.4" r="1.6" fill="#08202f"/>
        </svg>
      </span>
      <span class="plnl-brand__text">
        <span class="plnl-brand__word">PLNL</span>
        <span class="plnl-brand__cn">本德</span>
      </span>
    </a>
    <div class="plnl-links">
      <a href="https://plnl.vip">家庭控制台</a>
      <a href="https://mail.plnl.vip">域名邮箱</a>
      <a href="https://plnl.vip">文档</a>
      <a href="https://plnl.vip">服务状态</a>
    </div>
    <div class="plnl-bar__meta">
      <span>© 2026 PLNL · 本德</span>
      <a href="https://plnl.vip">plnl.vip</a>
      <a class="plnl-icp" href="https://beian.miit.gov.cn/" target="_blank" rel="noopener noreferrer">粤ICP备2024320296号
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">
          <path d="M14 4h6v6M20 4l-8.5 8.5" stroke-linecap="round" stroke-linejoin="round"/>
          <path d="M18 14v5a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V7a1 1 0 0 1 1-1h5" stroke-linecap="round"/>
        </svg>
      </a>
    </div>
  </div>
</footer>"""

SHELL = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>PLNL · 本德 — 页脚组件</title>
<link rel="stylesheet" href="footer.css" />
<style>
  *,*::before,*::after{box-sizing:border-box}
  body{
    margin:0;background:#02080e;color:#eef4f9;
    font-family:"Inter","PingFang SC","Hiragino Sans GB","Microsoft YaHei",system-ui,sans-serif;
    -webkit-font-smoothing:antialiased;
  }
  /* ---- 交付页自己的排版，与被交付的页脚无关 ---- */
  .spec-head{
    max-width:1180px;margin:0 auto;
    padding:clamp(48px,8vw,96px) clamp(20px,4vw,56px) clamp(32px,5vw,56px);
  }
  .spec-kicker{
    margin:0 0 14px;font-size:10.5px;letter-spacing:.34em;text-transform:uppercase;color:#5d7b8f;
  }
  .spec-head h1{
    margin:0 0 14px;font-family:"Songti SC","Noto Serif SC",Georgia,serif;
    font-size:clamp(30px,4.4vw,52px);font-weight:500;letter-spacing:.06em;line-height:1.24;
  }
  .spec-head p{max-width:52ch;margin:0;font-size:13.5px;line-height:1.95;color:#93aabd}
  .spec-tags{display:flex;flex-wrap:wrap;gap:8px;margin-top:22px;padding:0;list-style:none}
  .spec-tags li{
    padding:5px 11px;border-radius:999px;border:1px solid rgba(152,188,216,.18);
    font-size:11px;letter-spacing:.06em;color:#a9bfd0;
  }

  .spec-sec{position:relative;border-top:1px solid rgba(152,188,216,.10)}
  .spec-sec__bar{
    display:flex;align-items:baseline;gap:14px;flex-wrap:wrap;
    max-width:1180px;margin:0 auto;padding:26px clamp(20px,4vw,56px) 0;
  }
  .spec-sec__num{
    font-size:11px;letter-spacing:.2em;color:#4d6b80;
  }
  .spec-sec__bar h2{
    margin:0;font-size:14px;font-weight:500;letter-spacing:.06em;color:#cfe0ec;
  }
  .spec-sec__bar code{
    padding:2px 7px;border-radius:5px;background:rgba(142,198,234,.10);
    font-size:11px;color:#8ec6ea;
  }
  .spec-sec__note{margin:0 0 0 auto;font-size:11.5px;color:#6b8398}
  .spec-stage{padding-top:22px}
  .spec-stage--light{background:#ffffff}

  @media (max-width:640px){
    .spec-sec__note{margin-left:0;width:100%}
  }
</style>
</head>
<body>

<header class="spec-head">
  <p class="spec-kicker">PLNL · 本德 / 组件交付</p>
  <h1>站点页脚</h1>
  <p>
    围绕 <strong>PLNL</strong>、<strong>本德</strong> 与域名 <strong>plnl.vip</strong> 组织的三套页脚形态。
    深色是品牌基调，浅色给白底页面用，紧凑版给内容较轻的页面用。三套共用同一个 CSS 文件，改 <code>--f-*</code> 变量即可整体换肤。
  </p>
  <ul class="spec-tags">
    <li>备案号已按合规要求外链工信部</li>
    <li>WCAG AA 对比度</li>
    <li>键盘可达 / focus-visible</li>
    <li>无 JS · 无外部依赖</li>
  </ul>
</header>

<section class="spec-sec">
  <div class="spec-sec__bar">
    <span class="spec-sec__num">01</span>
    <h2>深色 · 完整版</h2>
    <code>.plnl-footer</code>
    <p class="spec-sec__note">默认形态，用于主站 / 控制台</p>
  </div>
  <div class="spec-stage">
__FULL__
  </div>
</section>

<section class="spec-sec">
  <div class="spec-sec__bar">
    <span class="spec-sec__num">02</span>
    <h2>浅色变体</h2>
    <code>.plnl-footer--light</code>
    <p class="spec-sec__note">白底页面、打印、文档站</p>
  </div>
  <div class="spec-stage spec-stage--light">
__LIGHT__
  </div>
</section>

<section class="spec-sec">
  <div class="spec-sec__bar">
    <span class="spec-sec__num">03</span>
    <h2>紧凑版</h2>
    <code>.plnl-footer--compact</code>
    <p class="spec-sec__note">一行搞定，适合登录页 / 单页</p>
  </div>
  <div class="spec-stage">
__COMPACT__
  </div>
</section>

</body>
</html>
"""

html = SHELL.replace("__FULL__", full.strip()).replace("__LIGHT__", light.strip()).replace("__COMPACT__", compact.strip())
(base / "index.html").write_text(html, encoding="utf-8")
print("index.html 已生成", len(html))
