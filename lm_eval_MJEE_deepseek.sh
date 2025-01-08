lm_eval --model openai-chat-completions \
    --model_args model=deepseek-chat,base_url=https://api.deepseek.com/v1/chat/completions,max_retries=3,num_concurrent=1,eos_string="</s>" \
    --tasks MJEE_logic_2023_shuffle \
    --apply_chat_template \
    --log_samples \
    --output_path /root/lm_eval_output \
    --wandb_args project=MJEE_logic_2023_deepseek_v3,name=deepseek-v3-shuffle \