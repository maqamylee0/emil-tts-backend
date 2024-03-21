from TTS.utils.manage import ModelManager
from TTS.utils.synthesizer import Synthesizer

path = "/home/emmilina/alx/tts/venv/lib/python3.10/site-packages/TTS/.models.json"

model_manager = ModelManager(path)

model_path, config_path, model_item = model_manager.download_model("tts_models/en/ljspeech/tacotron2-DDC")
print(f"pppppp{model_path}");
voc_path, voc_config_path, _ = model_manager.download_model(model_item["default_vocoder"])

syn = Synthesizer(
    tts_checkpoint=model_path,
    tts_config_path=config_path,
    vocoder_checkpoint=voc_path,
    vocoder_config=voc_config_path
)

text = "Is it hard to become a theoretical physicist? \
Obviously yes.I fully intended to do it. I was basically the smartest person I had ever met until I turned 17. I got a \
bachelor’s physics degree from MIT. I was fiercely motivated. I failed. I dropped out of a physics Ph.D. program after multiple attempts.\
So yes, it is hard.\
It’s even harder than you think. Getting a Ph.D. in physics still isn’t enough. Half of all physics students want to be theoreticians. Only five percent get to be,\
     there aren’t more jobs than that available. So even among Ph.D. physics graduates who want the job, only one in ten has what it takes to actually become a theoretical physicist.\
And academic talent is not enough. You also need people skills. A lot of physics is oral culture. There are a thousand absolutely vital facts for your progress that simply aren’t written down anywhere. You have to talk to your classmates, befriend your professors, I don’t know what all else. You can’t be a lone wolf. That’s pretty much called \
      a crackpot, in almost every case. (I think Quora has one or maybe two popular writers who break that mold.)\
I don’t know what people skills are required, but I sure as hell wish somebody had told me in advance that if I wasn’t going to be all chummy and best \
 pals with every physics \
student and every physics professor I met, not to bother showing up.\
Undergraduate physics student advisors, pay heed. Students deserve better than to waste years pursuing a goal simply because nobody ever bothered to tell them how different graduate “school”\
is from undergraduate.\
If I had it over again, knowing what I know now,\
I’m not sure I would even bother with a college degree at all, not even a bachelor’s, and I wouldn’t go to MIT; I’d just go somewhere easier for a couple of years, absolutely master all the intro classes, and then be a private tutor."

outputs = syn.tts(text)
syn.save_wav(outputs, "audio-1.wav")