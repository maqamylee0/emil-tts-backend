from TTS.utils.manage import ModelManager
from TTS.utils.synthesizer import Synthesizer

path = "/home/emmilina/alx/tts/venv/lib/python3.10/site-packages/TTS/.models.json"

model_manager = ModelManager(path)

model_path, config_path, model_item = model_manager.download_model("tts_models/en/ljspeech/tacotron2-DDC")
voc_path, voc_config_path, _ = model_manager.download_model(model_item["default_vocoder"])

syn=Synthesizer(
    tts_checkpoint=model_path,
    tts_config_path=config_path,
    vocoder_checkpoint=voc_path,
    vocoder_config=voc_config_path
)