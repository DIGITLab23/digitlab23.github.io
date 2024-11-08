---
title: "IH-GAN: A Conditional Generative Model for Implicit Surface-Based Inverse Design of Cellular Structures"
authors:
- Jun Wang
- Wei_Chen
- Daicong Da
- Mark Fuge
- Rahul Rai
date: "2022-05-23"
doi: "10.1016/j.cma.2022.115060"

# Schedule page publish date (NOT publication's date).
publishDate: "2022-05-23"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["article-journal"]

# Publication name and optional abbreviated publication name.
publication: "*Computer Methods in Applied Mechanics and Engineering, 396*"
publication_short: ""

abstract: Variable-density cellular structures can overcome connectivity and manufacturability issues of topologically optimized structures, particularly those represented as discrete density maps. However, the optimization of such cellular structures is challenging due to the multiscale design problem. Past work addressing this problem generally either only optimizes the volume fraction of single-type unit cells but ignoring the effects of unit cell geometry on properties, or considers the geometry–property relation but builds this relation via heuristics. In contrast, we propose a simple yet more principled way to accurately model the property to geometry mapping using a conditional deep generative model, named Inverse Homogenization Generative Adversarial Network (IH-GAN). It learns the conditional distribution of unit cell geometries given properties and can realize the one-to-many mapping from properties to geometries. We further reduce the complexity of IH-GAN by using the implicit function parameterization to represent unit cell geometries. Results show that our method can 1) generate various unit cells that satisfy given material properties with high accuracy ($R^2$-scores between target properties and properties of generated unit cells > 98%) and 2) improve the optimized structural performance over the conventional variable-density single-type structure. In the minimum compliance example, our IH-GAN generated structure achieves a 79.7% reduction in concentrated stress and an extra 3.03% reduction in displacement. In the target deformation examples, our IH-GAN generated structure reduces the target matching error by 86.4% and 79.6% for two test cases, respectively. We also demonstrated that the connectivity issue for multi-type unit cells can be solved by transition layer blending.

# Summary. An optional shortened abstract.
# summary: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis posuere tellus ac convallis placerat. Proin tincidunt magna sed ex sollicitudin condimentum.

# Display this page in the Featured widget?
featured: false

links:
- name: "Link"
  url: "https://www.sciencedirect.com/science/article/pii/S0045782522002699?via%3Dihub"
url_pdf: 'files/papers/2103.02588.pdf'
url_code: 'https://github.com/ideallab/ih-gan_cmame_2022'
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
