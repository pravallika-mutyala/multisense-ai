def build_fusion_prompt(user_text=None, image_caption=None, audio_text=None):
    prompt = "The following information comes from multiple modalities.\n\n"

    if image_caption:
        prompt += f"Image: {image_caption}\n\n"

    if audio_text:
        prompt += f"Audio: {audio_text}\n\n"

    if user_text:
        prompt += f"User Input: {user_text}\n\n"

    prompt += "Generate a clear, meaningful response that combines all inputs."
    return prompt
