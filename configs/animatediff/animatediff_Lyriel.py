# config for model
stable_diffusion_v15_url = 'runwayml/stable-diffusion-v1-5'
randomness = dict(
    seed=[
        10917152860782582783, 6399018107401806238, 15875751942533906793,
        6653196880059936551
    ],
    diff_rank_seed=True)

diffusion_scheduler = dict(
    type='DDIMScheduler',
    beta_end=0.012,
    beta_schedule='linear',
    beta_start=0.00085,
    num_train_timesteps=1000,
    prediction_type='epsilon',
    set_alpha_to_one=True,
    clip_sample=False,
    thresholding=False,
    steps_offset=1)

model = dict(
    type='AnimateDiff',
    vae=dict(
        type='AutoencoderKL',
        from_pretrained=stable_diffusion_v15_url,
        subfolder='vae'),
    unet=dict(
        type='UNet3DConditionMotionModel',
        unet_use_cross_frame_attention=False,
        unet_use_temporal_attention=False,
        use_motion_module=True,
        motion_module_resolutions=[1, 2, 4, 8],
        motion_module_mid_block=False,
        motion_module_decoder_only=False,
        motion_module_type='Vanilla',
        motion_module_kwargs=dict(
            num_attention_heads=8,
            num_transformer_block=1,
            attention_block_types=['Temporal_Self', 'Temporal_Self'],
            temporal_position_encoding=True,
            temporal_position_encoding_max_len=24,
            temporal_attention_dim_div=1),
        subfolder='unet',
        from_pretrained=stable_diffusion_v15_url),
    text_encoder=dict(
        type='ClipWrapper',
        clip_type='huggingface',
        pretrained_model_name_or_path=stable_diffusion_v15_url,
        subfolder='text_encoder'),
    tokenizer=stable_diffusion_v15_url,
    scheduler=diffusion_scheduler,
    test_scheduler=diffusion_scheduler,
    data_preprocessor=dict(type='DataPreprocessor'),
    motion_module_cfg=dict(
        path='/home/wangrunqi/AnimateDiff/models/Motion_Module/mm_sd_v14.ckpt'
    ),
    dream_booth_lora_cfg=dict(
        type='ToonYou',
        path='/home/wangrunqi/AnimateDiff/models/' +
        'DreamBooth_LoRA/lyriel_v16.safetensors',
        steps=25,
        guidance_scale=7.5))
