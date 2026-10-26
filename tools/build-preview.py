#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build-preview.py — 把 snippets/ 里的皮肤套到一个「模拟 SmarterMail 登录页」的壳里，
生成本地预览 HTML，方便在浏览器里直接看效果。

用法：
    python3 tools/build-preview.py snippets/v7-floating.html previews/v7-demo.html
    python3 tools/build-preview.py snippets/v6-glass-panel-photo.html out.html --system-bg

参数：
    --system-bg   让模拟页的容器自带一张明亮背景（模拟系统原来的照片）。
                  皮肤的背景层如果被容器压住，就会看到这个效果。
                  不加这个参数时容器透明，皮肤自己的背景才看得见。
"""
import sys
from pathlib import Path

SHELL = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>预览 · NameCraneLogin</title>
<style>
  /* ↓ 这一段模拟「系统原本的样式」，不是皮肤的一部分 */
  *{box-sizing:border-box}
  html{background:#f2f4f6}
  html,body{margin:0;height:100%;font-family:"Segoe UI","PingFang SC",Arial,sans-serif}
  body{background:transparent}
  #page{position:relative;min-height:100%;display:flex;align-items:center;justify-content:center;__PAGEBG__}
  .sm-card{width:300px;background:#fff;border-radius:3px;padding:26px 24px 18px;box-shadow:0 10px 40px rgba(0,0,0,.45);color:#333}
  .sm-card h1{margin:0 0 22px;font-size:15px;font-weight:400;text-align:center;color:#555}
  .sm-field{margin-bottom:16px}
  .sm-field label{display:block;font-size:11px;color:#c0392b;margin-bottom:4px}
  .sm-field input{width:100%;border:0;border-bottom:1px solid #c0392b;padding:4px 0;font-size:13px;outline:none}
  .sm-err{font-size:10.5px;color:#c0392b;margin-top:4px}
  .sm-row{display:flex;align-items:center;gap:8px;font-size:11.5px;color:#666;margin:14px 0 16px}
  .sm-toggle{width:30px;height:16px;border-radius:8px;background:#cfd4d8;position:relative}
  .sm-toggle:after{content:"";position:absolute;left:2px;top:2px;width:12px;height:12px;border-radius:50%;background:#fff}
  .sm-btn{display:block;margin-left:auto;background:#1b7fc4;color:#fff;border:0;border-radius:2px;font-size:12px;padding:7px 18px;cursor:pointer}
  .sm-cookie{position:fixed;left:0;right:0;bottom:0;background:rgba(40,40,40,.9);color:#eee;font-size:10.5px;padding:8px 14px;line-height:1.5}
</style>
</head>
<body>

  <!-- ===== 模拟：SmarterMail 登录页原有结构 ===== -->
  <div id="page">
    <div class="sm-card">
      <h1>欢迎使用 SmarterMail</h1>
      <div class="sm-field">
        <label>电子邮件地址 *</label>
        <input type="text" />
        <div class="sm-err">必填字段。</div>
      </div>
      <div class="sm-field">
        <label style="color:#666">密码 *</label>
        <input type="password" />
      </div>
      <div class="sm-row"><span class="sm-toggle"></span>记住我</div>
      <button class="sm-btn">登录</button>
    </div>
  </div>
  <div class="sm-cookie">一旦登录，即表示您接受此网站的 cookie　Webmail 无法兼容于私密或无限浏览模式。</div>
  <!-- ===== 模拟结构结束 ===== -->

  <!-- ↓↓↓ 下面粘的就是域设置里那段代码 ↓↓↓ -->
__SNIPPET__
  <!-- ↑↑↑ 皮肤结束 ↑↑↑ -->
</body>
</html>
"""

SYSTEM_BG = ('background-image:linear-gradient(115deg,#efece6 0%,#d9d0c3 26%,'
             '#b98b4e 48%,#8a5a2b 68%,#e8e2d8 100%)')


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        raise SystemExit(1)
    src, out = Path(sys.argv[1]), Path(sys.argv[2])
    snippet = src.read_text(encoding="utf-8")
    pagebg = SYSTEM_BG if "--system-bg" in sys.argv else "background:transparent"
    html = SHELL.replace("__PAGEBG__", pagebg).replace("__SNIPPET__", snippet)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    print(f"{out} 已生成（来源 {src}）")


if __name__ == "__main__":
    main()
