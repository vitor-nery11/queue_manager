import asyncio
import time

class RequisicaoIA:
    def __init__(
        self,
        id_req: int,
        prompt: str,
        modelo: str,
        tempo_estimado: float,
        status: str = "pendente",
    ) -> None:
        if prompt is None or prompt.strip() == '':
            raise ValueError('O prompt não pode ser vazio')

        self.id_req = id_req
        self.prompt = prompt
        self.modelo = modelo
        self.tempo_estimado = tempo_estimado
        self.status = status


class ProcessadorLote:
    def __init__(self, requisicoes: list[RequisicaoIA]) -> None:
        self.requisicoes = requisicoes

    async def processar_requisicao(self, req: RequisicaoIA) -> str:
        try:
            req.status = 'em andamento'
            await asyncio.sleep(req.tempo_estimado)
            req.status = 'concluido'
            return f'requisicao {req.id_req} ({req.modelo}): sucesso'
        except Exception:
            req.status = 'erro'
            return f'requisicao {req.id_req} ({req.modelo}): Erro de processamento'

    async def processar_todas(self) -> list[str]:
        return await asyncio.gather(
            *(self.processar_requisicao(req) for req in self.requisicoes)
        )

async def main():
    print(f'testando o processador de requisicoes IA...')

    #criando requisicao de teste
    req1 = RequisicaoIA(
        id_req=1,
        prompt='Explique python',
        modelo='GPT-4',
        tempo_estimado=1.5,
    )
    req2 = RequisicaoIA(
        id_req=2,
        prompt='Explique IA',
        modelo='Claude-3.5',
        tempo_estimado=2.0,
    )

    processador = ProcessadorLote([req1, req2])

    inicio = time.time()
    resultado = await processador.processar_todas()
    fim = time.time()

    print(f'--- Resultados do processamento ---')
    for res in resultado:
        print(res)

    print(f'Tempo total de processamento: {fim - inicio: .2f} segundos')
    print(f'Status Req 1: {req1.status}')
    print(f'Status Req 2: {req2.status}')



if __name__ == '__main__':
    asyncio.run(main())
