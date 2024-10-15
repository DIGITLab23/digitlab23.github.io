---
title: "Beyond the Known: Detecting Novel Feasible Domains over an Unbounded Design Space"
authors:
- Wei_Chen
- Mark Fuge
date: "2017-10-02"
doi: "10.1115/1.4037306"

# Schedule page publish date (NOT publication's date).
publishDate: "2017-10-02"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["article-journal"]

# Publication name and optional abbreviated publication name.
publication: "*Journal of Mechanical Design, 139*(11)"
publication_short: ""

abstract: To solve a design problem, sometimes it is necessary to identify the feasible design space. For design spaces with implicit constraints, sampling methods are usually used. These methods typically bound the design space; that is, limit the range of design variables. But bounds that are too small would fail to cover all possible designs; while bounds that are too large would waste sampling budget. This paper tries to solve the problem of efficiently discovering (possibly disconnected) feasible domains in an unbounded input data space. We propose a data-driven adaptive sampling technique -- epsilon-margin sampling, which both learns the domain boundary of feasible designs, while also expanding our knowledge of the design space as available budget increases. This technique is data-efficient, in that it makes principled probabilistic trade-offs between refining existing domain boundaries versus expanding the design space. We demonstrate that this method can better identify feasible domains on standard test functions compared to both random and active sampling (via uncertainty sampling). However, a fundamental problem when applying adaptive sampling to real world designs is that designs often have high dimensionality and thus require (in the worst case) exponentially more samples per dimension. We show how coupling Design Manifolds with epsilon-margin sampling allows us to actively expand high-dimensional design spaces without incurring this exponential penalty. We demonstrate this on real-world examples of glassware and bottle design, where our method discovers designs that have different appearance and functionality from its initial design set.

# Summary. An optional shortened abstract.
# summary: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis posuere tellus ac convallis placerat. Proin tincidunt magna sed ex sollicitudin condimentum.

# Display this page in the Featured widget?
featured: false

# links:
# - name: ""
#   url: ""
url_pdf: 'files/papers/md_139_11_111405.pdf'
url_code: 'https://github.com/IDEALLab/domain_expansion_jmd_2017'
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
image:
  caption: ''
  focal_point: ""
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: []

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: example
---
