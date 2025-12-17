---
layout: home
title: 🏠 Home
nav_exclude: false
nav_order: 1
---

# {{ site.tagline }}

{: .mb-2 }
{{ site.description }}
{: .fs-6 .fw-300 }

{{ site.staffersnobio }}

<!-- {: .success }
>Peter's class will be on Zoom today, Wednesday, November 26th. Please see the pinned post on [Campuswire](https://campuswire.com/c/GF283E889/feed/551) for details of how to join!-->

<!--{: .success }
>Welcome to DSC 10! Make sure to read this website thoroughly and complete the items in the [Getting Started](https://dsc10.com/syllabus/#-getting-started) checklist. These are due very soon, on **Saturday, September 27th at 11:59PM**.-->

<!--{: .warning }
This site is **under construction**. Anything you read here is not finalized. This disclaimer will be removed when the site is ready for Fall 2025. -->

<!--{: .success }
>The Final Exam is **this Saturday, June 7th from 11:30AM to 2:30PM in CENTER 101**.
>
>Earn 1 participation point by filling out both [SETs](https://academicaffairs.ucsd.edu/Modules/Evals/) and the internal [End-of-Quarter Survey](https://forms.gle/hWqgRBp4B45LDMLW9) before Saturday, June 7th at 8AM.
-->

<!--{: .success }
>**Tip**: When working on assignments, use Ctrl+F on this page to search for a keyword and quickly find the relevant lecture. Click the "✏️ write" button to open a static version of the lecture for reference, which is much faster than loading it on DataHub.
>
>Also, make sure to use the [reference sheet](https://dsc-courses.github.io/bpd-reference/docs/documentation/intro/) to quickly look up `babypandas` methods and see examples of how they work.
-->

[Jump to the current week](/#week-10-review){: .btn }

{% for module in site.modules %}
{{ module }}
{% endfor %}
