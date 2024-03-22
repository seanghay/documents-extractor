from doctr.models import ocr_predictor

text_extractor = ocr_predictor(
    det_arch="db_resnet50",
    reco_arch="vitstr_base",
    pretrained=True,
    detect_orientation=True,
    assume_straight_pages=False,
    export_as_straight_boxes=True,
    straighten_pages=True,
  )