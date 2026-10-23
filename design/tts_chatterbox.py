#!/usr/bin/env python3
"""Chatterbox TTS helper for build_video.py (MIT licence, runs on CPU).

Reads a JSON list of [text, wav_path] pairs and writes one WAV per line, loading the
model once. It runs in its own Python environment because Chatterbox needs PyTorch.

  python3 tts_chatterbox.py lines.json [reference.wav]

Without a reference clip it uses Chatterbox's default voice. A reference clip copies
that speaker's voice and accent, so only use a recording you have the rights to.
Every output carries Resemble AI's inaudible Perth watermark.
"""
import json, sys
import torch, torchaudio as ta
from chatterbox.tts import ChatterboxTTS

pairs = json.load(open(sys.argv[1]))
ref = sys.argv[2] if len(sys.argv) > 2 else None
m = ChatterboxTTS.from_pretrained(device="cuda" if torch.cuda.is_available() else "cpu")
for text, path in pairs:
    w = m.generate(text, audio_prompt_path=ref, exaggeration=0.5, cfg_weight=0.5)
    ta.save(path, w, m.sr)
    print(path, flush=True)
