from CholaBot import CholaBot
import logging

# Define o arquivo que trará os logs de execução
logDeExecucao = logging.FileHandler(
    filename='discordBot.log', encoding='utf-8', mode='w'
)

logging.basicConfig(
    handlers=[logDeExecucao],
    level=logging.DEBUG
)

if __name__ == "__main__":
    bot = CholaBot(log_handler=logDeExecucao)
    bot.iniciar()
