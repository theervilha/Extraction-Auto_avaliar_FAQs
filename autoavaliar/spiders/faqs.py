import scrapy
from bs4 import BeautifulSoup

class FAQExtractor(scrapy.Spider):
	name = 'FAQExtractor'
	start_urls = [
		'https://autoavaliar.movidesk.com/kb'
	]
	urls = ["https://autoavaliar.movidesk.com/kb/article/94614/atividades-economicas-do-cnpj-aceita-no-cadastro-para-compras-cn?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/94679/por-alguma-eventualidade-posso-desistir-da-compra?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/185024/como-atualizar-um-boleto-vencido?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/94620/como-buscar-veiculos-de-meu-interesse-de-forma-rapida?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/168473/aplicativo-mensagem-nao-foi-possivel-carregar-a-lista-de-avali?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/94619/os-veiculos-da-auto-avaliar-sao-de-leilao?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/130744/limpar-dados-da-tabela-de-veiculos-mmvv-no-app-auto-avaliar?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/128090/criacao-de-usuario-no-sistema-de-avaliacao-usbi?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/97691/como-limpar-os-dados-do-aplicativo-auto-avaliar?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/94606/como-acessar-a-area-lojista-compras?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/94670/o-que-e-o-autopay?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/180395/nao-estou-visualizando-os-anuncios-de-um-grupo-de-concessionaria?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/97082/cadastro-de-veiculos-no-correio-motors?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/168495/aceitar-recebimento-de-mensagens-whatsapp-suporte?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/165497/alterar-status-de-avaliacao-pelo-usbi?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/61191/inserir-participante-em-um-grupo-de-anuncio-ou-cotacao?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/123496/inserir-ou-remover-um-lojista-participante-em-um-grupo-de-anunci?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/94657/existe-uma-cobranca-mensal-no-site-lojista?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/128097/localizar-codigo-dms-apollo?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/133658/atualizacao-de-estoque-autosync-integrador?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/142347/diferenca-no-resultado-da-busca-de-quantidades-de-veiculos-vendi?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/136135/analise-da-equipe-de-sync-integracao-em-uma-avaliacao-nao-integr?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/137734/correio-motors-como-emitir-nota-fiscal-de-pecas-pelo-correio-m?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/158356/como-alterar-minha-senha-do-usbi?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/128095/localizar-codigo-dms-nbs?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/136633/anunciar-via-autosync-em-portais-nao-homologados-ou-sites?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/156178/cadastro-de-usuarios-b2b-adm?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/176203/como-faco-para-anunciar?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/165488/erro-origin-is-required?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/92151/criar-pacote-lote-de-veiculos?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/128094/localizar-codigo-dms-dealer-workflow?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/92154/bem-vindo-a-nossa-faq?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/137804/correio-motors-erro-0-5001-ao-tentar-emitir-uma-nota-fiscal?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/169810/correio-motors-imprimir-recibo-de-venda-apos-o-veiculo-ter-sid?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/170269/correio-motors-lock-wait-timeout-exceeded-try-restarting-trans?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/180400/alem-da-taxa-da-auto-avaliar-existe-alguma-outra-taxa?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/94622/onde-acompanho-o-tempo-restante-da-publicacao?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/94621/onde-encontro-mais-informacoes-sobre-o-veiculo?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/96635/como-cancelar-uma-venda-feita-no-auto-avaliar?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/97089/emissao-nf-de-entrada-compra-no-correio-motors?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/93334/auto-avaliar-lojista?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/97100/correio-motors-veiculos?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/142523/criacao-e-acompanhamento-de-tickets-no-movidesk?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/93336/usbi-sistema-de-avaliacao?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/169538/correio-motors-erro-lost-connection-to-mysql-server-during-que?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/172655/como-limpar-o-cache-dns?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/133665/auto-sync?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/165859/sla-departamento-de-suporte?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/92145/suporte-remoto?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/96709/como-conferir-as-vendas-concluidas?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/97092/lancamento-de-despesas-no-correio-motors?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/128105/localizar-codigo-dms-sync?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/93335/auto-avaliar-anunciante-adm?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/176199/como-faco-para-me-cadastrar?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/198843/utilizacao-do-portal-de-seminovos-toyota?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/61232/tabela-cst-codigo-situacao-tributaria?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/93331/aplicativo-de-avaliacoes?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/140112/correio-motors-erro-parametros-parametros-de-icms-tbestados?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/137801/correio-motors-erro-0-6006-ao-tentar-emitir-uma-nota-fiscal?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/137729/correio-motors-erro-ao-emitir-nota-fiscal-de-pecas-codigo-cest?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/142522/criacao-de-usuario-no-movidesk?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/169819/correio-motors-recibo-de-venda-proposta-nao-encontrada?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/180396/posso-comprar-utilizando-o-cpf?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/180399/voces-entregam-o-carro?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/94652/onde-posso-acompanhar-ofertas-lances-e-anuncios?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/94623/quais-as-formas-de-avaliar-enviar-um-valor-no-veiculo-anunciado?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/96636/como-conferir-anuncios-em-andamento?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/96704/como-revalidar-anuncios-que-expiraram?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/97093/criar-proposta-para-venda-no-correio-motors?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/107026/correio-motors-rejeicao-nf-e-501-pedido-de-cancelamento-in?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/128096/localizar-codigo-dms-sisdia?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/132288/integracao-de-avaliacoes-com-dms-e-como-verificar-o-status?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/169537/correio-motors-erro-falha-na-assinatura-o-conjunto-de-chaves-n?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/176702/correio-motors-erro-656-consumo-indevido?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/176205/como-faco-para-alterar-meu-endereco-de-e-mail?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/176204/como-faco-para-utilizar-uma-carta-de-credito?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/177842/correio-motors-cadastro-de-tipos-de-documentospendencias-do-ve?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/180390/meu-cadastro-no-site-da-auto-avaliar-foi-aprovado-mas-nao-estou?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/198842/seminovos-toyota-abradit-frota-certificada-toyota?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/151782/e-possivel-anexar-fotos-do-celular-no-aplicativo?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/128091/localizar-codigo-dms-dealer-windows?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/97081/cadastro-e-consulta-de-clientes-fornecedores-e-bancos?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/104032/limpar-cache-do-navegador?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/94693/como-alterar-as-informacoes-do-meu-perfil?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/128104/localizar-codigo-dms-sercon?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/174989/tela-de-relatorios-desconfigurada?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/96637/como-anunciar-um-veiculo-no-auto-avaliar?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/96682/conferir-lances-e-ofertas-recebidas-no-anuncio?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/95617/recuperar-senha-aplicativo-auto-avaliar?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/95604/recuperar-a-senha-auto-avaliar-adm?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/190418/e-possivel-alterar-a-placa-cadastrada?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/188126/por-que-ha-diferenca-no-relatorio-exportado-no-arquimedes?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/91687/recuperar-senha-de-acesso-ecossistema?ticketId=&q=",
	"https://autoavaliar.movidesk.com/kb/article/94617/eu-nao-me-lembro-dos-dados-de-acesso-ao-site-lojista?ticketId=&q=",
	]

	def parse(self, response):
		for url in self.urls:
			yield scrapy.Request(response.urljoin(url), callback=self.getContentFAQ)

	def getContentFAQ(self, response):
		html = response.css(".article-content").get()
		content = BeautifulSoup(html, "html.parser").text
		print(content)
		return {'index_name': 'autoavaliar', 'items': content}