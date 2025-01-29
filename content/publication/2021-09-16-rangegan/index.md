---
title: "Range-Constrained Generative Adversarial Network: Design Synthesis Under Constraints Using Conditional Generative Adversarial Networks"
authors:
- Amin Heyrani Nobari
- Wei_Chen
- Faez Ahmed
date: "2021-09-16"
doi: "10.1115/1.4052442"

# Schedule page publish date (NOT publication's date).
publishDate: "2021-09-16"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["article-journal"]

# Publication name and optional abbreviated publication name.
publication: "*Journal of Mechanical Design, 144*(2)"
publication_short: ""

abstract: Typical engineering design tasks require the effort to modify designs iteratively until they meet certain constraints, i.e., performance or attribute requirements. Past work has proposed ways to solve the inverse design problem, where desired designs are directly generated from specified requirements, thus avoiding the trial and error process. Among those approaches, the conditional deep generative model shows great potential since (1) it works for complex high-dimensional designs and (2) it can generate multiple alternative designs given any range condition. In this work, we propose a conditional deep generative model, range-constrained generative adversarial network, to achieve automatic design synthesis subject to range constraints. The proposed model addresses the sparse conditioning issue in data-driven inverse design problems by introducing a label-aware self-augmentation approach. We also propose a new uniformity loss to ensure the generated designs evenly cover the given requirement range. Through a real-world example of constrained 3D shape generation, we show that the label-aware self-augmentation leads to an average improvement of 14% on the constraint satisfaction for generated 3D shapes, and the uniformity loss leads to a 125% average increase on the uniformity of generated shapes’ attributes. This work laid the foundation for data-driven inverse design problems where we consider range constraints and there are sparse regions in the condition space.

# Summary. An optional shortened abstract.
# summary: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis posuere tellus ac convallis placerat. Proin tincidunt magna sed ex sollicitudin condimentum.

# Display this page in the Featured widget?
featured: false

links:
- name: "Link"
  url: "https://asmedigitalcollection.asme.org/mechanicaldesign/article/144/2/021708/1119623/Range-Constrained-Generative-Adversarial-Network"
url_pdf: ''
url_code: 'https://github.com/ahnobari/Range-GAN'
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
