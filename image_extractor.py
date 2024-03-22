import json
import numpy as np
import torch
import os
from doctr.models import ocr_predictor
from doctr.io import DocumentFile
from glob import glob
from tqdm import tqdm


class NumpyFloatValuesEncoder(json.JSONEncoder):
  def default(self, obj):
    if isinstance(obj, np.float32):
      return float(obj)
    return json.JSONEncoder.default(self, obj)


def main():
  device = "cuda" if torch.cuda.is_available() else "cpu"
  text_extractor = ocr_predictor(
    det_arch="db_resnet50",
    reco_arch="vitstr_base",
    pretrained=True,
    detect_orientation=True,
    assume_straight_pages=False,
    export_as_straight_boxes=True,
    straighten_pages=True,
  )

  text_extractor = text_extractor.to(device)
  text_extractor.eval()

  found_files = list(glob("photos/**/*.jpg", recursive=True))
  found_files.extend(glob("photos/**/*.jpeg", recursive=True))
  found_files.extend(glob("photos/**/*.png", recursive=True))

  for image_file in tqdm(found_files):
    out_file = os.path.join("result", image_file + ".json")
    if os.path.exists(out_file):
      continue

    images = DocumentFile.from_images(image_file)
    image = images[0]
    out = text_extractor([image])

    os.makedirs(os.path.dirname(out_file), exist_ok=True)

    with open(out_file, "w") as outfile:
      json.dump(
        out.pages[0].export(),
        outfile,
        cls=NumpyFloatValuesEncoder,
        ensure_ascii=False,
        indent=2,
      )

if __name__ == "__main__":
  main()
