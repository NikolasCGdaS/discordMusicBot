import datetime
import json

# Define a classe Cog de comandos básicos
class FrequencyService:

    # Instância de variáveis
    def __init__(self):
        #self.bot = bot
        self.movimentationLog = []
        self.outputFile = "channelMovementLog.json"

    # Função de adição de registro a tabela temporária
    def eventRegister(self, member, connectionType, entryChannel, exitChannel):
        
        userId = str(member.id)
        userName=member.name
        if member.nick:
            userName = member.nick

        now = datetime.datetime.now()
        timestamp = now.strftime("%d/%m/%Y %H:%M:%S") # Formata como DD/MM/AAAA HH:MM:SS

        register = {
            "User_id": userId,
            "User": userName,
            "Connection_Type": connectionType,
            "TimeStamp": timestamp,
            "Entry_Channel": entryChannel,
            "Exit_Channel": exitChannel,
            "Log_id": None
        }

        self.movimentationLog.append(register)

        if len(self.movimentationLog) % 50 ==0:
            self.jsonConvert()
        
        return timestamp

    # Função para transformar estrutura de dados formada em json
    def jsonConvert(self):
        try:
            with open(self.outputFile, 'w', encoding='utf-8') as f:
                json.dump(self.movimentationLog, f, indent=4, ensure_ascii=False)
            print(f"Dados salvos com sucesso em {self.outputFile}")
        except Exception as e:
            print(f"Erro ao salvar o JSON: {e}")

    # Verifica entrada de usuário em canal
    #@commands.Cog.listener()
    #async def on_voice_state_update(self, member, before, after):

    #     now = datetime.datetime.now()
    #     timestamp = now.strftime("%d/%m/%Y %H:%M:%S") # Formata como DD/MM/AAAA HH:MM:SS
    #     # Entrou em um canal sem estar em nenhum antes
    #     if before.channel is None and after.channel is not None:
    #         self.eventRegister(
    #             member, 
    #             "ENTRADA", 
    #             after.channel.name, 
    #             "N/A"
    #         )
    #         mensagem = f"{member.name} de id {member.id} entrou em {after.channel.name} às {timestamp}."
    #         print(mensagem)

    #     # Saiu de um canal para nenhum
    #     elif before.channel is not None and after.channel is None:
    #         self.eventRegister(
    #             member, 
    #             "SAIDA", 
    #             "N/A",
    #             before.channel.name
    #         )
    #         mensagem = f"{member.name} de id {member.id} saiu de {before.channel.name} às {timestamp}."
    #         print(mensagem)

    #     # Saiu e um canal para entrar em outro
    #     elif before.channel is not None and after.channel != before.channel:
    #         self.eventRegister(
    #             member, 
    #             "TROCA", 
    #             after.channel.name, 
    #             before.channel.name
    #         )
    #         mensagem = f"{member.name} de id {member.id} saiu de {before.channel.name} para {after.channel.name} {timestamp}."
    #         print(mensagem)

    # @commands.command(name='upJs')
    # async def uploadJson_command(self, ctx):
    #     self.jsonConvert()
    #     await ctx.send(f"Log de voz salvo em {self.outputFile}.")


# Função de configuração para carregar o Cog
#async def setup(bot):
#    await bot.add_cog(frequencyService(bot))