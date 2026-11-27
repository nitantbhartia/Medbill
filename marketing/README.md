# marketing/

Scripts that make marketing videos from BillKarma's published data. Nothing in the deployed app imports
this folder and Railway does not run it.

- `expose_san_diego/`: "City ER Price Expose, Part 1: San Diego". `expose_san_diego_facts.json` holds every
  number shown, with its source. `python3 render.py stills` draws five check frames; `python3 render.py video`
  writes `out/billkarma_expose_san_diego_v1.mp4` and a contact sheet. Needs Pillow, numpy, ffmpeg and the Inter fonts.
