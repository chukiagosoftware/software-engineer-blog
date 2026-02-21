---
title: "Home"
---


Debug: Total posts: {{ len (where .Site.RegularPages ".Type" "posts") }}

{{ range first 3 (where .Site.RegularPages ".Type" "posts") }}
{{ .Render "summary" }}
{{ end }}