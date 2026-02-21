---
title: "Home"
---


{{ range first 3 (where .Site.RegularPages ".Type" "posts") }}
{{ .Render "summary" }}
{{ end }}