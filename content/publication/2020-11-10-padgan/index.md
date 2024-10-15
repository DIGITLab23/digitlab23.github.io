---
title: "PaDGAN: Learning to Generate High-Quality Novel Designs"
authors:
- Wei_Chen
- Faez Ahmed
date: "2020-11-10"
doi: "10.1115/1.4048626"

# Schedule page publish date (NOT publication's date).
publishDate: "2020-11-10"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["article-journal"]

# Publication name and optional abbreviated publication name.
publication: "*Journal of Mechanical Design, 143*(3)"
publication_short: ""

abstract: Deep generative models are proven to be a useful tool for automatic design synthesis and design space exploration. When applied in engineering design, existing generative models face three challenges&#58; (1) generated designs lack diversity and do not cover all areas of the design space, (2) it is difficult to explicitly improve the overall performance or quality of generated designs, and (3) existing models generally do not generate novel designs, outside the domain of the training data. In this article, we simultaneously address these challenges by proposing a new determinantal point process-based loss function for probabilistic modeling of diversity and quality. With this new loss function, we develop a variant of the generative adversarial network, named "performance augmented diverse generative adversarial network" (PaDGAN), which can generate novel high-quality designs with good coverage of the design space. By using three synthetic examples and one real-world airfoil design example, we demonstrate that PaDGAN can generate diverse and high-quality designs. In comparison to a vanilla generative adversarial network, on average, it generates samples with a 28\% higher mean quality score with larger diversity and without the mode collapse issue. Unlike typical generative models that usually generate new designs by interpolating within the boundary of training data, we show that PaDGAN expands the design space boundary outside the training data towards high-quality regions. The proposed method is broadly applicable to many tasks including design space exploration, design optimization, and creative solution recommendation.

# Summary. An optional shortened abstract.
# summary: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis posuere tellus ac convallis placerat. Proin tincidunt magna sed ex sollicitudin condimentum.

# Display this page in the Featured widget?
featured: false

# links:
# - name: ""
#   url: ""
url_pdf: 'files/papers/md_143_3_031703.pdf'
url_code: 'https://github.com/wchen459/PaDGAN'
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
