---
# Leave the homepage title empty to use the site title
title:
date: 2022-10-24
type: landing

sections:
  # Hero: always dark, with grid + glow background (styled in assets/scss/custom.scss)
  - block: markdown
    content:
      text: |
        <div class="hero-tech-inner">
        <span class="hero-eyebrow"><span class="hero-dot"></span><span class="d-none d-md-inline">Design Innovation &amp; Generative Intelligence Lab</span><span class="d-md-none">DIGIT Lab</span> · Texas A&amp;M</span>
        <h1 class="hero-tech-title">AI that designs better <span class="text-gradient">materials, structures &amp; machines</span>.</h1>
        <p class="hero-tech-lead">The DIGIT Lab builds AI that goes beyond model performance and efficiency to make engineering design more complex, trustworthy, discoverable and creative.</p>
        <div class="hero-tech-ctas">
        <a class="btn btn-glow" href="research/">Explore our research <i class="fas fa-arrow-right"></i></a>
        <a class="btn btn-ghost" href="join/">Join the lab</a>
        </div>
        <div class="hero-tags"><span>design ideation</span><span>generative design</span><span>design for X</span></div>
        {{< lab_stats extra_value="2" extra_label="NSF awards" >}}
        </div>
    design:
      css_class: hero-tech

  # Research pillars as cards
  - block: features
    content:
      title: Four questions drive our work
      subtitle: We develop computational methods for design ideation, generative design, and design for X (manufacturing, sustainability, reliability, and beyond) across diverse engineering domains.
      items:
        - name: Complexity
          icon: diagram-project
          icon_pack: fas
          description: How can AI unlock design complexities that are fundamentally inaccessible to traditional methods?
        - name: Trustworthiness
          icon: shield-halved
          icon_pack: fas
          description: How can we develop AI-driven design methodologies that engineers can trust?
        - name: Discoverability
          icon: magnifying-glass-chart
          icon_pack: fas
          description: How can AI discover new knowledge that expands human understanding and guides design innovation?
        - name: Creativity
          icon: lightbulb
          icon_pack: fas
          description: How can AI enable "out-of-the-box" design solutions and become a true inventor?
    design:
      css_class: pillars

  - block: collection
    content:
      title: Latest News
      subtitle:
      text:
      count: 5
      filters:
        author: ''
        category: ''
        exclude_featured: false
        publication_type: ''
        tag: ''
      offset: 0
      order: desc
      page_type: news
    design:
      view: compact
      columns: '1'
      css_class: news-tech

  # Closing call-to-action
  - block: markdown
    content:
      text: |
        <div class="cta-card">
        <span class="hero-eyebrow">// We're building the team</span>
        <h2>Help turn AI into an engineering inventor.</h2>
        <p>Meet the people behind the research, or find out how to join us.</p>
        <div class="hero-tech-ctas">
        <a class="btn btn-glow" href="people/">Meet the team <i class="fas fa-arrow-right"></i></a>
        <a class="btn btn-ghost" href="join/">Open positions</a>
        </div>
        </div>
    design:
      columns: '1'
      css_class: cta-section
---
