import argparse
from lm_eval.__main__ import cli_evaluate, setup_parser

def main():
    # 创建参数解析器
    parser = setup_parser()

    # 模拟命令行参数
    command_line_args = [
        "--model", "openai-chat-completions",
        "--model_args", "model=deepseek-chat,base_url=https://api.deepseek.com/v1/chat/completions,max_retries=3,num_concurrent=1,eos_string=</s>",
        "--tasks", "MJEE_logic_2023_shuffle",
        "--apply_chat_template",
        "--log_samples",
        "--output_path", "/root/lm_eval_output",
    ]
    args = parser.parse_args(command_line_args)

    # 调用评估函数
    cli_evaluate(args)

if __name__ == "__main__":
    main()
