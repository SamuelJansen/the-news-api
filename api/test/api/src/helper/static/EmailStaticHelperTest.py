from python_helper import Constant as c
from python_helper import ObjectHelper, StringHelper, Test
from api.src.constant import NewsConstant
from api.src.helper.static import EmailStaticHelper


ARRANGED = "arranged"
EXPECTED = "expected"
EMAILS_ARRANGED_AND_EXPECTED_LIST = [
    {
        ARRANGED: """para pensar

bom dia. a argentina aumentou sua taxa de juros para 52% ontem. comparando, estamos ótimos. na vida, faz sentido se comparar com quem está pior? o comodismo pode te impedir de querer melhorar.

Vai ficar mais fácil trabalhar em PortugalMUNDO

(Imagem: Reuters | Reprodução)

Deu vontade? Enquanto você coloca sua playlist favorita para se animar, Portugal está fazendo algo a mais para dar um fôlego extra à sua economia.  O país vai acelerar a emissão de vistos de imigrantes [https://g1.globo.com/mundo/noticia/2022/06/16/portugal-deve-acelerar-emissao-de-vistos-para-atrair-mais-trabalhadores.ghtml?utm_source=thenewscc&utm_medium=email&utm_campaign=referral]  para trabalhadores estrangeiros [https://g1.globo.com/mundo/noticia/2022/06/16/portugal-deve-acelerar-emissao-de-vistos-para-atrair-mais-trabalhadores.ghtml?utm_source=thenewscc&utm_medium=email&utm_campaign=referral].

Portugal tem enfrentado escassez de mão de obra, especialmente no setor de hospitalidade e turismo, um de seus principais motores econômicos.

O projeto permite que estrangeiros busquem emprego por 120 dias,  simplifica o processo de migração familiar [https://www1.folha.uol.com.br/mundo/2022/06/portugal-encaminha-pacotao-de-vistos-e-cria-permissao-especial-a-quem-procura-trabalho.shtml?utm_source=thenewscc&utm_medium=email&utm_campaign=referral], cria permissões especiais para  nômades digitais [https://www1.folha.uol.com.br/mundo/2022/06/portugal-encaminha-pacotao-de-vistos-e-cria-permissao-especial-a-quem-procura-trabalho.shtml?utm_source=thenewscc&utm_medium=email&utm_campaign=referral] e facilita o processo para cidadãos dos países de língua portuguesa.

A relevância 🇧🇷

Os brasileiros estão na liderança como a maior comunidade imigrante em território português, representando  29% dos estrangeiros em situação regular no país [https://www1.folha.uol.com.br/mundo/2022/06/portugal-encaminha-pacotao-de-vistos-e-cria-permissao-especial-a-quem-procura-trabalho.shtml?utm_source=thenewscc&utm_medium=email&utm_campaign=referral].

No entanto, como muitos imigrantes chegam como turistas e começam a trabalhar ilegalmente, os números reais são maiores. Aos simplificar a autorização, será mais fácil controlar as condições dos trabalhadores estrangeiros.

O que mais é destaque mundialmente falando?

Clima tenso em Quito.  Manifestantes bloqueiam acesso à capital do Equador [https://g1.globo.com/mundo/noticia/2022/06/16/manifestantes-bloqueiam-acesso-a-capital-do-equador-apesar-de-apelo-ao-dialogo-por-parte-do-governo.ghtml?utm_source=thenewscc&utm_medium=email&utm_campaign=referral]

Conflito geopolítico.  Líderes europeus fazem visita inédita à Ucrânia [https://g1.globo.com/mundo/noticia/2022/06/16/lideres-europeus-fazem-visita-inedita-a-ucrania.ghtml?utm_source=thenewscc&utm_medium=email&utm_campaign=referral]

Ainda na Europa...  Ações europeias atingem mínima de 16 meses após aumentos de juros [https://www.infomoney.com.br/mercados/acoes-europeias-atingem-minima-de-16-meses-apos-aumentos-de-juros/]

Os gamers já podem comemorar 👾BRASIL

(Imagem: Philippe Wojazer | Reprodução)

Redução de tributos. Enquanto muitos jogadores aproveitaram o feriado para passar de nível nos seus games preferidos, o presidente Jair Bolsonaro editou, ontem, um novo decreto que  reduziu os impostos sobre jogos eletrônicos [https://agenciabrasil.ebc.com.br/geral/noticia/2022-06/presidente-anuncia-nova-reducao-de-impostos-para-jogos-eletronicos?utm_source=thenewscc&utm_medium=email&utm_campaign=referral].

Na prática… A partir de julho, a alíquota de importação de partes e acessórios dos consoles e das máquinas de videogame cairá de 16% para 12%.

No caso de videogames com telas incorporadas — o Nintendo DS entraria aqui? —, a alíquota será zerada.

Essa é, na verdade, a 4ª redução de impostos para videogames [https://www.tecmundo.com.br/voxel/240468-bolsonaro-anuncia-4-reducao-impostos-video-games.htm?utm_source=thenewscc&utm_medium=email&utm_campaign=referral]. Em agosto de 2021, o Imposto sobre Produtos Industrializados (IPI) desses produtos já tinha diminuído.

O objetivo: De acordo com o governo federal, as reduções buscam incentivar o desenvolvimento do segmento de jogos eletrônicos no país,  um mercado com expectativa para ultrapassar os US$ 200 bilhões, globalmente, até 2023 [https://forbes.com.br/forbes-tech/2022/01/com-2022-decisivo-mercado-de-games-ultrapassara-us-200-bi-ate-2023/?utm_source=thenewscc&utm_medium=email&utm_campaign=referral].

O que mais é destaque no país?

Bruno Pereira e Dom Phillips:  Avião com restos mortais chega a Brasília para perícia [https://g1.globo.com/df/distrito-federal/noticia/2022/06/16/bruno-pereira-e-dom-phillips-aviao-com-restos-mortais-chega-a-brasilia.ghtml?utm_source=thenewscc&utm_medium=email&utm_campaign=referral]

Varíola dos macacos.  Brasil tem seis casos confirmados da doença [https://www.cnnbrasil.com.br/saude/brasil-tem-seis-casos-confirmados-de-variola-dos-macacos/?utm_source=thenewscc&utm_medium=email&utm_campaign=referral]

Fundo eleitoral:  Veja como será a divisão dos R$ 4,9 bilhões entre os partidos [https://g1.globo.com/mg/triangulo-mineiro/noticia/2022/06/16/video-operadores-de-drone-afirmam-que-jogavam-veneno-em-cima-de-publico-em-evento-de-lula-e-kalil-em-mg-jogou-2-litros-so.ghtml?utm_source=thenewscc&utm_medium=email&utm_campaign=referral]

Só falta todo mundo mudar o nome para TikTok

TECNOLOGIA

(GIF: Tenor | Reprodução)

Pode copiar, só não faz igual. Já faz tempo que as redes sociais estão buscando replicar o sucesso do “aplicativo vizinho”, mas o desejo está cada vez mais escancarado.

Facebook: Nesta semana, vazou um memorando do diretor do Facebook dizendo, de forma clara, que  vão tornar o feed mais parecido com o TikTok [https://www.theverge.com/2022/6/15/23168887/facebook-discovery-engine-redesign-tiktok?utm_source=thenewscc&utm_medium=email&utm_campaign=referral].

Instagram: A rede está testando  um novo modelo de tela cheia para seu feed [https://www.theverge.com/2022/6/16/23170210/instagram-full-screen-video-feed-another-test-tiktok-competition?utm_source=thenewscc&utm_medium=email&utm_campaign=referral], em mais uma perseguição ao formato do tico-teco.

Twitter: Elon Musk disse aos funcionários da empresa, ontem,  que ela precisa se tornar mais parecida com o WeChat e o TikTok [https://www.theverge.com/2022/6/16/23171054/elon-musk-twitter-deal-1-billion-users-wechat-tiktok?utm_source=thenewscc&utm_medium=email&utm_campaign=referral] para atingir 1 bilhão de usuários.

Nesse processo, as redes sociais ficam com funcionalidades cada vez mais parecidas. Quem gostava do Instagram só com fotos está se sentindo órfão.

Já o original…

Enquanto todos tentam copiá-lo, o TikTok está se aprimorando. A rede chinesa está testando  um novo recurso que permite aos usuários ver quais de seus seguidores visualizaram seus vídeos [https://techcrunch.com/2022/06/16/tiktok-testing-feature-see-which-followers-viewed-your-posts/?utm_source=thenewscc&utm_medium=email&utm_campaign=referral]. Agora vão saber quando você estiver stalkeando. risos.

Compre cripto ao som dos canhões! 💣

PATROCINADO POR MONETT

Compre ao som dos canhões e venda ao som dos violinos. É nos momentos de baixa do mercado que surgem as  melhores oportunidades [https://monett.co/mbm-janela-cripto-400-chainlink/?xcode=VD-NEWS-MBM-ALL-20220617-EMKT-JK1-VSL-JK1&utm_source=NEWS&utm_medium=EMKT&utm_content=MBM&utm_campaign=VD-NEWS-MBM-ALL-20220617-EMKT-JK1-VSL-JK1].

Guerra na Ucrânia, inflação e juros altos nos EUA, investidores fugindo de ativos arriscados… Vários motivos estão fazendo as criptomoedas caírem nos últimos meses.

Para te incentivar a  aproveitar este momento [https://monett.co/mbm-janela-cripto-400-chainlink/?xcode=VD-NEWS-MBM-ALL-20220617-EMKT-JK1-VSL-JK1&utm_source=NEWS&utm_medium=EMKT&utm_content=MBM&utm_campaign=VD-NEWS-MBM-ALL-20220617-EMKT-JK1-VSL-JK1], duas empresas se uniram em uma campanha sensacional: O aplicativo de investimentos  Monett [https://monett.co/mbm-janela-cripto-400-chainlink/?xcode=VD-NEWS-MBM-ALL-20220617-EMKT-JK1-VSL-JK1&utm_source=NEWS&utm_medium=EMKT&utm_content=MBM&utm_campaign=VD-NEWS-MBM-ALL-20220617-EMKT-JK1-VSL-JK1] e o Mercado Bitcoin (MB) — maior corretora de cripto da América Latina.

Você ganha 3 vezes:

Com as  carteiras recomendadas [https://monett.co/mbm-janela-cripto-400-chainlink/?xcode=VD-NEWS-MBM-ALL-20220617-EMKT-JK1-VSL-JK1&utm_source=NEWS&utm_medium=EMKT&utm_content=MBM&utm_campaign=VD-NEWS-MBM-ALL-20220617-EMKT-JK1-VSL-JK1] e acesso ao plano mais completo da Monett;

Com  cashback [https://monett.co/mbm-janela-cripto-400-chainlink/?xcode=VD-NEWS-MBM-ALL-20220617-EMKT-JK1-VSL-JK1&utm_source=NEWS&utm_medium=EMKT&utm_content=MBM&utm_campaign=VD-NEWS-MBM-ALL-20220617-EMKT-JK1-VSL-JK1] para você investir em cripto;

Quando as criptos retomarem e chegar a hora de  colocar os lucros no bolso [https://monett.co/mbm-janela-cripto-400-chainlink/?xcode=VD-NEWS-MBM-ALL-20220617-EMKT-JK1-VSL-JK1&utm_source=NEWS&utm_medium=EMKT&utm_content=MBM&utm_campaign=VD-NEWS-MBM-ALL-20220617-EMKT-JK1-VSL-JK1].

É a sua chance de entrar em cripto com uma segurança e facilidade para aproveitar as oportunidades do momento. Só tem um problema: A campanha está quase acabando.  Veja esse vídeo para saber como não perder essa chance única [https://monett.co/mbm-janela-cripto-400-chainlink/?xcode=VD-NEWS-MBM-ALL-20220617-EMKT-JK1-VSL-JK1&utm_source=NEWS&utm_medium=EMKT&utm_content=MBM&utm_campaign=VD-NEWS-MBM-ALL-20220617-EMKT-JK1-VSL-JK1].

Um Round 6 na vida real

ENTRETENIMENTO

(Imagem: Netflix | Reprodução)

Direto do streaming. Se você não assistiu à Round 6, saiba que foi um dos poucos: a série foi o maior lançamento global da história da Netflix na sua estreia, com 111 milhões de espectadores em menos de um mês.

O programa de sucesso envolve uma série de jogos, que servirão de inspiração para um  reality show com prêmio de US$ 4,56 milhões [https://www.seudinheiro.com/2022/empresas/round-6-reality-show-netflix-inscricoes-miql/?utm_source=thenewscc&utm_medium=email&utm_campaign=referral].

Já que a ficção sul-coreana não é muito tranquila, a Netflix prometeu que não vai colocar em risco a vida dos 456 participantes, a serem escolhidos.

Na série, inspirada nas lutas financeiras após a crise de 2008, os jogadores arriscam suas vidas em jogos infantis mortais por um prêmio em dinheiro.

A estratégia… 🍿

Em primeiro lugar, a Netflix está criando  o maior evento de competição real de todos os tempos [https://www.seudinheiro.com/2022/empresas/round-6-reality-show-netflix-inscricoes-miql/?utm_source=thenewscc&utm_medium=email&utm_campaign=referral] — com uma recompensa em dinheiro nunca antes vista.

Mas, além disso, a notícia veio três dias depois do anúncio da segunda temporada de série. Certamente, o reality vai impulsionar a audiência.

Quer se inscrever?  Basta ter mais de 21 anos, um passaporte e falar inglês [https://www.squidgamecasting.com/?utm_source=thenewscc&utm_medium=email&utm_campaign=referral].

Sua empresa é orientada a dados?

PATROCINADO POR CREDITAS @ WORK

Vivemos a Era dos Dados. Todos precisam se adequar e passar a agir com base em análises sólidas, e o RH não fica fora disso — a alta competitividade por talentos está mostrando que  ser data driven é essencial. [https://www.creditas.com/beneficios/materiais-ricos/manual-rh-analitico?utm_medium=patrocinio&utm_source=ebook-rh-analitico-thenews&utm_campaign=atwork-b2b_ebook-rh-analitico-thenews_patrocinio_e-book&utm_term=20220617&utm_content=e-book]

Se você acha que um RH orientado a dados será menos humano, não se engane.  Ele continua humano, porém, se torna mais estratégico. [https://www.creditas.com/beneficios/materiais-ricos/manual-rh-analitico?utm_medium=patrocinio&utm_source=ebook-rh-analitico-thenews&utm_campaign=atwork-b2b_ebook-rh-analitico-thenews_patrocinio_e-book&utm_term=20220617&utm_content=e-book]

Mas, você sabe quais são os principais indicadores do RH? Dentre alguns, estão feedbacks da equipe, clima organizacional e taxa de turnover —mas há muitos outros.

Se você quer saber como ter um  RH analítico [https://www.creditas.com/beneficios/materiais-ricos/manual-rh-analitico?utm_medium=patrocinio&utm_source=ebook-rh-analitico-thenews&utm_campaign=atwork-b2b_ebook-rh-analitico-thenews_patrocinio_e-book&utm_term=20220617&utm_content=e-book] para atrair e engajar colaboradores em busca de melhores resultados,  esse e-book 100% gratuito da Creditas [https://www.creditas.com/beneficios/materiais-ricos/manual-rh-analitico?utm_medium=patrocinio&utm_source=ebook-rh-analitico-thenews&utm_campaign=atwork-b2b_ebook-rh-analitico-thenews_patrocinio_e-book&utm_term=20220617&utm_content=e-book] vai te salvar a vida!  Baixe clicando aqui [https://www.creditas.com/beneficios/materiais-ricos/manual-rh-analitico?utm_medium=patrocinio&utm_source=ebook-rh-analitico-thenews&utm_campaign=atwork-b2b_ebook-rh-analitico-thenews_patrocinio_e-book&utm_term=20220617&utm_content=e-book].

Você compraria um “vencidinho”?

ECONOMIA

(Imagem: Leandro Fonseca | Reprodução)

Economia polêmica. Com a inflação nas alturas, colocar no carrinho os “vencidinhos” — produtos próximos da data de validade, que são vendidos mais baratos —,  tem sido visto como uma boa opção para os brasileiros [https://jovempan.com.br/programas/jornal-da-manha/vencidinho-vira-opcao-para-economizar-mas-exige-cuidados-e-ainda-gera-duvidas.html?utm_source=thenewscc&utm_medium=email&utm_campaign=referral].

Para se ter uma ideia, em São Paulo, alguns produtos nessas condições chegam a custar metade do preço.

Sei não, viu dênius… Muitos têm receio na hora de consumir alimentos próximos da data de vencimento, mas, segundo médicos,  esse prazo indica que o produto vai perdendo alguns nutrientes [https://jovempan.com.br/programas/jornal-da-manha/vencidinho-vira-opcao-para-economizar-mas-exige-cuidados-e-ainda-gera-duvidas.html?utm_source=thenewscc&utm_medium=email&utm_campaign=referral], mas não significa que não pode ser consumido.

Os estabelecimentos, no entanto,  devem redobrar os cuidados de conservação dos “vencidinhos" [https://jovempan.com.br/programas/jornal-da-manha/vencidinho-vira-opcao-para-economizar-mas-exige-cuidados-e-ainda-gera-duvidas.html?utm_source=thenewscc&utm_medium=email&utm_campaign=referral], principalmente em relação à temperatura.

Zoom Out: Além do preço mais camarada, a proposta de vender alimentos perto do vencimento também ajuda a evitar o desperdício de comida.  O brasileiro, em média, desperdiça cerca de 60 quilos de comida por ano [https://jovempan.com.br/programas/jornal-da-manha/vencidinho-vira-opcao-para-economizar-mas-exige-cuidados-e-ainda-gera-duvidas.html?utm_source=thenewscc&utm_medium=email&utm_campaign=referral].

O poder de investir é seu

PATROCINADO POR ÍON ITAÚ

íon Itaú [https://app.adjust.com/jsr?url=https%3A%2F%2Fv9v8.adj.st%2Facompanhamento-relatorios-home%3Fadj_t%3Dyb15lh7%26adj_deep_link%3Dionitau%253A%252F%252F%26adj_redirect%3Dhttps%253A%252F%252Fion.itau%252F%26adj_campaign%3Dthe_news]. A sua nova experiência de investimentos, ideal para acompanhar o dinheiro de perto e se informar sobre o mercado financeiro. Conheça o fundo Hashdex Cripto Selection e invista a partir de R$ 1.  Clique aqui e baixe o app [https://app.adjust.com/jsr?url=https%3A%2F%2Fv9v8.adj.st%2Facompanhamento-relatorios-home%3Fadj_t%3Dyb15lh7%26adj_deep_link%3Dionitau%253A%252F%252F%26adj_redirect%3Dhttps%253A%252F%252Fion.itau%252F%26adj_campaign%3Dthe_news].

Continua em clima de feriado?

DICAS DO FINAL DE SEMANA

(GIF: Acegif | Reprodução)

Muita gente está igual ao Homer Simpson hoje. Se você emendou o feriado ou ainda está ralando, aproveite: as dicas são o nosso presente para o seu final de semana. 🙌

Você preferiria morrer quando tem de morrer ou não morrer nunca mais? Esse é um dos questionamento que  Clóvis de Barros traz nesse podcast [https://www.youtube.com/watch?v=iTFuK50vY_s]. Pode ser legal de ouvir. 🎧

A tecnologia mudou o amor? Apesar de todas as particularidades do mundo atual,  nesse TED [https://www.ted.com/talks/helen_fisher_technology_hasn_t_changed_love_here_s_why?utm_source=thenewscc&utm_medium=email&utm_campaign=referral], você verá que os princípios básicos do amor continuam os mesmos.

Pra quem estava com saudade… A Netflix disponibilizou a última temporada da série  Peaky Blinders [https://www.netflix.com/br/title/80002479?utm_source=thenewscc&utm_medium=email&utm_campaign=referral]. Aproveite para maratonar.🍿

Clássico dos clássicos. Baseando-se nos habitantes da cidade mais próspera do seu tempo, o livro  O homem mais rico da Babilônia [https://www.amazon.com.br/Homem-Mais-Rico-Babil%C3%B4nia/dp/8595081530/ref=sr_1_5?keywords=livros+mais+vendidos&qid=1655420963&sr=8-5&utm_source=thenewscc&utm_medium=email&utm_campaign=referral] dá lições sobre riquezas e problemas financeiros.📚

Paixão nacional. Com essa receita de  empadinha de frango [https://www.panelinha.com.br/receita/Empadinha-de-frango?utm_source=thenewscc&utm_medium=email&utm_campaign=referral] você pode praticar à vontade, deixando a massa no ponto perfeito. 👨‍🍳

Para quem gosta de MPB. Chico Buarque está lançando, hoje, seu primeiro single inédito em 5 anos. Clique para escutar ' Que tal um samba? [https://open.spotify.com/artist/6tOsSffQQIXmK8TqsDck8t?si=bCwWWyiaRA2OhvI0IKT90Q]' assim que estiver disponível. 🎶

Você vai mesmo perder essa chance?SUPER GIVEAWAY

Só hoje, no último dia do nosso super giveaway, você ganha CHANCES EM DOBRO pra concorrer a um iPhone 13 novo.

Até às 23:59 de hoje (16), sua indicação vale por duas: 1 amigo = 2 chances. 2 amigos = 4 chances... 5 amigos = 10 chances. E assim vai.

Vai ficar de fora dessa? Pra ganhar chances em dobro vale tudo: mandar o link nos grupos dos amigos, postar nos stories e muito mais. Abuse da criatividade. risos.

Clique no botão abaixo, pegue seu link exclusivo de indicação e compartilhe. O seu iPhone pode estar a caminho ... Vai que vai!!!

CLIQUE PARA COMPARTILHAR [https://grow.surf/x5eg0s]

PS:  Clique aqui [https://thenews.substack.com/p/c6f5b3c7-6098-459d-9956-73077583f444?s=w] para visualizar as regras oficiais do sorteio.

O estagiário precisa de uma ajudinha…

PESQUISA THE NEWS

O chefe já deu o papo: Se o estagiário não souber quem são os leitores do dênius, vai dar ruim pra ele. Salvar o estagiário só depende de você.  É só clicar aqui para responder algumas perguntinhas em  [https://docs.google.com/forms/d/e/1FAIpQLScCjM0C7iywFiCbezMsjmcqEozwCtOyCRWUyK5bNE6GY3zo3w/viewform?usp=sf_link] apenas 3 minutos [https://docs.google.com/forms/d/e/1FAIpQLScCjM0C7iywFiCbezMsjmcqEozwCtOyCRWUyK5bNE6GY3zo3w/viewform?usp=sf_link].

the news 📬

Mais inteligente em 5 minutos. Somos um jornal gratuito e diário, que tem por objetivo te trazer tudo que você precisa saber para começar o seu dia bem e informado.

Notícias, de fato, relevantes sobre as principais atualidades do mundo, do Brasil, tecnologia e do mercado financeiro, sempre nessa ordem.

Direto na sua caixa de entrada do e-mail favorito, sempre às 06:06. É gratuito, mas pode viciar.

🎟️  O próximo anunciante pode ser você.  É só clicar aqui [https://thenewscc.typeform.com/to/twCcjR bQ].

já conhece nossas outras newsletters?

🦄  the bizness [https://thenewscc.com.br/bizness/]: sua dose de conteúdo sobre os assuntos mais relevantes do mundo dos negócios. análises, números e insights.  um MBA em forma de e-mail. [https://thenewscc.com.br/bizness/]

🏆  the champs [https://thenewscc.com.br/champs/]: todo o não óbvio sobre os esportes, na palma da sua mão.  descontraído e direto ao ponto, como deve ser [https://thenewscc.com.br/champs/].

🧸  the stories [https://thenewscc.com.br/stories/]: histórias que emocionam. não tão longas quanto  um romance, mas suficientes pra te fazer sentir.  contamos e escrevemos amor. [https://thenewscc.com.br/stories/]

até amanhã

Sempre chegamos a sua caixa de entrada por volta das 06:06. Alguns servidores de e-mail são teimosos e atrasam… Outros são piores ainda e nos jogam para o spam e/ ou promoções. Sempre que não nos encontrar na caixa de entrada, procure nessas duas.

[https://twitter.com/thenews_br]                               mais inteligente em 5 minutos.

the news.cc | newsletter

São Paulo, SP 04506-000 | Miami, FL

Política de Privacidade [https://drive.google.com/file/d/1Yi-bty-sLL5mCBwiDWKlE2JNLDclCmVe/view?usp=sharing] |  Anuncie conosco [https://thenewscc.typeform.com/to/twCcjRbQ]

Actualizar preferências https://thenews.updatemyprofile.com/t-qkyikly-AF625213-ykhdduoju-td  |   Remover subscrição https://thenews.cmail20.com/t/t-u-qkyikly-ykhdduoju-th/
""",
        EXPECTED: [
            "para pensar.",
            "bom dia. a argentina aumentou sua taxa de juros para 52% ontem. comparando, estamos ótimos. na vida, faz sentido se comparar com quem está pior? o comodismo pode te impedir de querer melhorar.",
            "MUNDO",
            "Vai ficar mais fácil trabalhar em Portugal.",
            "Deu vontade? Enquanto você coloca sua playlist favorita para se animar, Portugal está fazendo algo a mais para dar um fôlego extra à sua economia. O país vai acelerar a emissão de vistos de imigrantes para trabalhadores estrangeiros.",
            "Portugal tem enfrentado escassez de mão de obra, especialmente no setor de hospitalidade e turismo, um de seus principais motores econômicos.",
            "O projeto permite que estrangeiros busquem emprego por 120 dias, simplifica o processo de migração familiar, cria permissões especiais para nômades digitais e facilita o processo para cidadãos dos países de língua portuguesa.",
            "A relevância 🇧🇷",
            "Os brasileiros estão na liderança como a maior comunidade imigrante em território português, representando 29% dos estrangeiros em situação regular no país.",
            "No entanto, como muitos imigrantes chegam como turistas e começam a trabalhar ilegalmente, os números reais são maiores. Aos simplificar a autorização, será mais fácil controlar as condições dos trabalhadores estrangeiros.",
            "O que mais é destaque mundialmente falando?",
            "Clima tenso em Quito. Manifestantes bloqueiam acesso à capital do Equador.",
            "Conflito geopolítico. Líderes europeus fazem visita inédita à Ucrânia.",
            "Ainda na Europa… Ações europeias atingem mínima de 16 meses após aumentos de juros.",
            "BRASIL",
            "Os gamers já podem comemorar 👾",
            "Redução de tributos. Enquanto muitos jogadores aproveitaram o feriado para passar de nível nos seus games preferidos, o presidente Jair Bolsonaro editou, ontem, um novo decreto que reduziu os impostos sobre jogos eletrônicos.",
            "Na prática… A partir de julho, a alíquota de importação de partes e acessórios dos consoles e das máquinas de videogame cairá de 16% para 12%.",
            "No caso de videogames com telas incorporadas — o Nintendo DS entraria aqui? —, a alíquota será zerada.",
            "Essa é, na verdade, a 4ª redução de impostos para videogames. Em agosto de 2021, o Imposto sobre Produtos Industrializados (IPI) desses produtos já tinha diminuído.",
            "O objetivo: De acordo com o governo federal, as reduções buscam incentivar o desenvolvimento do segmento de jogos eletrônicos no país, um mercado com expectativa para ultrapassar os US$ 200 bilhões, globalmente, até 2023.",
            "O que mais é destaque no país?",
            "Bruno Pereira e Dom Phillips: Avião com restos mortais chega a Brasília para perícia.",
            "Varíola dos macacos. Brasil tem seis casos confirmados da doença.",
            "Fundo eleitoral: Veja como será a divisão dos R$ 4,9 bilhões entre os partidos.",
            "TECNOLOGIA",
            "Só falta todo mundo mudar o nome para TikTok.",
            "Pode copiar, só não faz igual. Já faz tempo que as redes sociais estão buscando replicar o sucesso do “aplicativo vizinho”, mas o desejo está cada vez mais escancarado.",
            "Facebook: Nesta semana, vazou um memorando do diretor do Facebook dizendo, de forma clara, que vão tornar o feed mais parecido com o TikTok.",
            "Instagram: A rede está testando um novo modelo de tela cheia para seu feed, em mais uma perseguição ao formato do tico-teco.",
            "Twitter: Elon Musk disse aos funcionários da empresa, ontem, que ela precisa se tornar mais parecida com o WeChat e o TikTok para atingir 1 bilhão de usuários.",
            "Nesse processo, as redes sociais ficam com funcionalidades cada vez mais parecidas. Quem gostava do Instagram só com fotos está se sentindo órfão.",
            "Já o original…",
            "Enquanto todos tentam copiá-lo, o TikTok está se aprimorando. A rede chinesa está testando um novo recurso que permite aos usuários ver quais de seus seguidores visualizaram seus vídeos. Agora vão saber quando você estiver stalkeando. risos.",
            "ENTRETENIMENTO",
            "Um Round 6 na vida real.",
            "Direto do streaming. Se você não assistiu à Round 6, saiba que foi um dos poucos: a série foi o maior lançamento global da história da Netflix na sua estreia, com 111 milhões de espectadores em menos de um mês.",
            "O programa de sucesso envolve uma série de jogos, que servirão de inspiração para um reality show com prêmio de US$ 4,56 milhões.",
            "Já que a ficção sul-coreana não é muito tranquila, a Netflix prometeu que não vai colocar em risco a vida dos 456 participantes, a serem escolhidos.",
            "Na série, inspirada nas lutas financeiras após a crise de 2008, os jogadores arriscam suas vidas em jogos infantis mortais por um prêmio em dinheiro.",
            "A estratégia… 🍿",
            "Em primeiro lugar, a Netflix está criando o maior evento de competição real de todos os tempos — com uma recompensa em dinheiro nunca antes vista.",
            "Mas, além disso, a notícia veio três dias depois do anúncio da segunda temporada de série. Certamente, o reality vai impulsionar a audiência.",
            "Quer se inscrever? Basta ter mais de 21 anos, um passaporte e falar inglês.",
            "ECONOMIA",
            "Você compraria um “vencidinho”?",
            "Economia polêmica. Com a inflação nas alturas, colocar no carrinho os “vencidinhos” — produtos próximos da data de validade, que são vendidos mais baratos —, tem sido visto como uma boa opção para os brasileiros.",
            "Para se ter uma ideia, em São Paulo, alguns produtos nessas condições chegam a custar metade do preço.",
            "Sei não, viu dênius… Muitos têm receio na hora de consumir alimentos próximos da data de vencimento, mas, segundo médicos, esse prazo indica que o produto vai perdendo alguns nutrientes, mas não significa que não pode ser consumido.",
            "Os estabelecimentos, no entanto, devem redobrar os cuidados de conservação dos “vencidinhos', principalmente em relação à temperatura.",
            "Zoom Out: Além do preço mais camarada, a proposta de vender alimentos perto do vencimento também ajuda a evitar o desperdício de comida. O brasileiro, em média, desperdiça cerca de 60 quilos de comida por ano.",
            "DICAS DO FINAL DE SEMANA",
            "Continua em clima de feriado?",
            "Muita gente está igual ao Homer Simpson hoje. Se você emendou o feriado ou ainda está ralando, aproveite: as dicas são o nosso presente para o seu final de semana. 🙌",
            "Você preferiria morrer quando tem de morrer ou não morrer nunca mais? Esse é um dos questionamento que. Clóvis de Barros traz nesse podcast. Pode ser legal de ouvir. 🎧",
            "A tecnologia mudou o amor? Apesar de todas as particularidades do mundo atual, nesse TED, você verá que os princípios básicos do amor continuam os mesmos.",
            "Pra quem estava com saudade… A Netflix disponibilizou a última temporada da série. Peaky Blinders. Aproveite para maratonar.🍿",
            "Clássico dos clássicos. Baseando-se nos habitantes da cidade mais próspera do seu tempo, o livro. O homem mais rico da Babilônia dá lições sobre riquezas e problemas financeiros.📚",
            "Paixão nacional. Com essa receita de empadinha de frango você pode praticar à vontade, deixando a massa no ponto perfeito. 👨‍🍳",
            "Para quem gosta de MPB. Chico Buarque está lançando, hoje, seu primeiro single inédito em 5 anos. Clique para escutar ' Que tal um samba? ' assim que estiver disponível. 🎶"
        ]
    },
    {
        ARRANGED: """relaxa

bom dia. hoje, o estagiário acordou sem inspiração e não conseguiu elaborar mensagem motivacional. às vezes, quando bate o cansaço, a única solução é um happy hour com os amigos.

Uma onda de renúncias na Europa?MUNDO

(Imagem: Reuters | Reprodução)

Boris Johnson fez escola. O primeiro-ministro italiano, Mario Draghi, formalizou ontem um pedido de renúncia do cargo, a exemplo do que seu semelhante inglês fez na semana passada.

Só que o presidente do país  simplesmente rejeitou o pedido [https://www.cnnbrasil.com.br/internacional/primeiro-ministro-da-italia-diz-que-ira-renunciar/?utm_source=thenewscc&utm_medium=e-mail&utm_campaign=referral] e o aconselhou a se apresentar ao Parlamento, para melhor entender sua situação política.

O que está acontecendo? Mario Draghi perdeu apoio do principal partido da sua base de governo, o Movimento 5 Estrelas, que  boicotou uma das votações dos pacotes propostos por ele [https://g1.globo.com/mundo/noticia/2022/07/14/primeiro-ministro-da-italia-mario-draghi-renuncia-ao-cargo.ghtml?utm_source=thenewscc&utm_medium=e-mail&utm_campaign=referral], desencadeando a crise.

O boicote. O premiê propôs medidas para conter o impacto da inflação e apresentou um projeto para a construção de um incinerador de lixo. Fazendo críticas às propostas, o partido discordou do italiano.

A realidade é que Draghi não precisa do apoio do partido para se manter no poder, porque tem  ampla maioria no parlamento [https://www1.folha.uol.com.br/mundo/2022/07/primeiro-ministro-da-italia-anuncia-renuncia-apos-implosao-de-coalizao-governista.shtml?utm_source=thenewscc&utm_medium=e-mail&utm_campaign=referral]. Mas, para o político, não faz sentido ser premiê sem o apoio do M5E.

A crise está instaurada na terra da pizza e a situação terá que ser bem costurada. Ao contrário do que aconteceu no Reino Unido, a maioria dos italianos quer continuar com a liderança do primeiro-ministro. Mais discreto, né? risos.

O que mais é destaque mundialmente falando?

Retratos da guerra.  Ataques russos deixaram mais de 20 mortos no centro da Ucrânia [https://g1.globo.com/mundo/ucrania-russia/noticia/2022/07/14/ataques-russos-deixam-12-mortos-no-centro-da-ucrania.ghtml?utm_source=thenewscc&utm_medium=e-mail&utm_campaign=referral]

Conflito secreto?  Israel e Irã estão desvelando várias ações clandestinas que realizam um contra o outro [https://www.bbc.com/portuguese/internacional-62067419?utm_source=thenewscc&utm_medium=e-mail&utm_campaign=referral]

Cuidado.  Homem morre depois de tomar uma garrafa inteira de licor em apenas dois minutos [https://g1.globo.com/mundo/noticia/2022/07/14/homem-morre-apos-ingerir-uma-garrafa-inteira-de-licor-em-dois-minutos.ghtml?utm_source=thenewscc&utm_medium=e-mail&utm_campaign=referral]

De PEC em PECBRASIL

(Imagem: Veja | Reprodução)

Muito trabalho em Brasília. Se tem um assunto que o pessoal da política tem falado neste ano é sobre as PECs. Depois de tantos votos para mudanças na Constituição, os congressistas bateram um recorde em 2022.

Este ano foi o que  mais teve PECs aprovadas em toda a história da Lei Maior [https://www.poder360.com.br/historia/2022-bate-recorde-de-mudancas-na-constituicao/?utm_source=thenewscc&utm_medium=e-mail&utm_campaign=referral], nos seus longos e bem vividos 33 anos de promulgação, com 11 alterações ao texto constitucional — até agora.

Looking back. O Brasil tem uma grande tradição de inovações constitucionais. O período em que houve mais mudanças foi no governo de Jair Bolsonaro, com 26, seguido pelo primeiro mandato de Dilma Rousseff, com 17.

Só para comparar: Os Estados Unidos, que são conhecidos por ter uma Constituição bem enxuta, aprovou  apenas 27 alterações nos seus 233 anos [https://oglobo.globo.com/politica/constituicao-dos-eua-teve-27-emendas-em-230-anos-23581420?utm_source=thenewscc&utm_medium=e-mail&utm_campaign=referral] de existência. O Brasileiro é realmente cheio de opiniões. risos.

E por falar nisso… Ontem,  f [https://g1.globo.com/politica/noticia/2022/07/14/com-presenca-de-bolsonaro-congresso-promulga-emenda-que-permite-pacote-social-pre-eleitoral.ghtml?utm_source=thenewscc&utm_medium=e-mail&utm_campaign=referral] oi promulgada a  [https://g1.globo.com/politica/noticia/2022/07/14/com-presenca-de-bolsonaro-congresso-promulga-emenda-que-permite-pacote-social-pre-eleitoral.ghtml?utm_source=thenewscc&utm_medium=e-mail&utm_campaign=referral] Emenda Constitucional Kamikaze [https://g1.globo.com/politica/noticia/2022/07/14/com-presenca-de-bolsonaro-congresso-promulga-emenda-que-permite-pacote-social-pre-eleitoral.ghtml?utm_source=thenewscc&utm_medium=e-mail&utm_campaign=referral], que autoriza o estado de emergência no país e libera um gasto público de R$ 41,2 bilhões.

Outras notícias importantes no país:

Polêmica no Rio Grande do Sul.  Juíza eleitoral afirmou que a bandeira do Brasil seria considerada uma propaganda para o Governo Bolsonaro [https://veja.abril.com.br/coluna/radar/juiza-eleitoral-diz-que-bandeira-do-brasil-virou-simbolo-de-bolsonaro/?utm_source=thenewscc&utm_medium=e-mail&utm_campaign=referral]

Qualidade do ensino.  7 das 10 melhores universidades da América Latina estão no Brasil [https://www.cnnbrasil.com.br/nacional/sete-das-dez-melhores-universidades-na-america-latina-estao-no-brasil-veja-lista/?utm_source=thenewscc&utm_medium=e-mail&utm_campaign=referral]

Excelente para PPPs.  Brasil foi eleito um dos melhores ambientes para se estabelecer parcerias público-privadas [https://www.abdib.org.br/2022/07/13/brasil-tem-um-dos-melhores-ambientes-para-ppp-na-america-latina/?utm_source=thenewscc&utm_medium=e-mail&utm_campaign=referral]

TikTok e Instagram estão ameaçando o Google Maps

TECNOLOGIA

(GIF: Tenor | Reprodução)

A geração Z não gosta de mapas. Um novo estudo mostrou que  40% dos jovens não vão ao Google Maps [https://www.tecmundo.com.br/redes-sociais/241822-tiktok-instagram-ameacando-google-maps-busca.htm?utm_source=email&utm_campaign=thenewscc&utm_id=referral] quando procuram um lugar para almoçar — eles vão para o TikTok ou Instagram.

Com a descoberta, a ameaça do aplicativo chinês aos negócios do Google não se limita apenas ao Youtube, impactando também os serviços de Pesquisa e Mapas.

A explicação: O Google Maps foi feito com a intenção de levar mapas de papel para o computador. O objetivo faz sentido para quem cresceu sem GPS, mas fica distante da realidade dos adolescentes que nunca viram um mapa de papel.

Segundo os executivos do Google, em vez de digitar palavras-chave, essa nova geração procura descobrir conteúdo de  maneiras novas e mais imersivas [https://techcrunch.com/2022/07/12/google-exec-suggests-instagram-and-tiktok-are-eating-into-googles-core-products-search-and-maps/?utm_source=email&utm_campaign=thenewscc&utm_id=referral].

Por que isso é relevante? Embora os usuários mais velhos da Internet não usem o tico-teco para encontrar um restaurante, essa tendência pode  reduzir o negócio principal do Google de pesquisa e descoberta ao longo do tempo [https://techcrunch.com/2022/07/12/google-exec-suggests-instagram-and-tiktok-are-eating-into-googles-core-products-search-and-maps/?utm_source=email&utm_campaign=thenewscc&utm_id=referral].

Tentando afastar o Google Maps dos mapas de papel, a empresa está incorporando realidade aumentada e outras inovações no sistema — será que é suficiente pra atrair a gen Z?

Com essa seleção, você vai subir de cargo

PATROCINADO POR AMAZON

Esses produtos que achamos na Amazon te farão trabalhar melhor, ser mais produtivo e ter mais resultados — todas as condições para você ser promovido. risos.

💻 Sua postura agradece.  Esse suporte para notebook custa só R$ 54 e vai fazer seu trabalho bem mais confortável. [https://amzn.to/3o1ZQJM]

👊 Seu punho também…  Um desconto de 18% em um mouse pad como esse não pode passar batido [https://amzn.to/3IDsTge]. Para você que digita o dia todo, é essencial.

📚 Ler faz bem para a carreira:  Do autor de Como Fazer Amigos e Influenciar Pessoas, esse livro vai te ensinar a fazer sua carreira decolar [https://amzn.to/3O4u3m9]. Está com 45% OFF!

🎧 Suas calls sem ruídos e fios atrapalhando.  Com esses fones, suas reuniões vão ficar melhores e você vai poder colocar aquela música de fundo para te ajudar a focar. [https://amzn.to/3yIDaU4]

🖥️ Melhore sua mesa.  Nunca vimos um produto tão simples mas capaz de organizar sua mesa, delimitar  o seu espaço e deixá-lo esteticamente mais bonito [https://amzn.to/3yD0mmF]. Vale conferir!

Clique aqui [https://amzn.to/3uNviiG] e veja tudo o que a loja de Jeff Bezos tem para você.

Enquanto a OpenSea entra no inverno cripto, o Itaú acredita no verão

NEGÓCIOS

(Imagem: Anton Petrus | Getty Images))

Deve ser a diferença entre os hemisférios. A OpenSea — o maior mercado para negociar NFTs do mundo — parece ter visto que a febre das fotos de perfil de macacos passou e  demitiu 20% de sua equipe ontem [https://techcrunch.com/2022/07/14/nft-marketplace-opensea-lays-off-20-percent-of-its-staff-we-have-entered-crypto-winter/?utm_source=thenewscc&utm_medium=email&utm_campaign=referral].

O CEO da startup não mediu suas palavras e afirmou que a empresa entrou num inverno criptográfico sem precedentes, somado à instabilidade da economia.

O medo é claro. Uma desaceleração no crescimento,  depois de uma avaliação de US$ 13,3 bilhões [https://techcrunch.com/2022/07/14/nft-marketplace-opensea-lays-off-20-percent-of-its-staff-we-have-entered-crypto-winter/?utm_source=thenewscc&utm_medium=email&utm_campaign=referral] com a corrida de alta da criptomoeda de 2021.

(Imagem: Pinterest | Reprodução)

Falando em tokens e mudando de estação… No mesmo dia das demissões da OpenSea,  o Itaú anunciou que está aderindo [https://www.infomoney.com.br/mercados/itau-lanca-plataforma-de-tokenizacao-de-ativos/?utm_source=thenewscc&utm_medium=email&utm_campaign=referral]   [https://www.infomoney.com.br/mercados/itau-lanca-plataforma-de-tokenizacao-de-ativos/?utm_source=thenewscc&utm_medium=email&utm_campaign=referral] à tokenização [https://www.infomoney.com.br/mercados/itau-lanca-plataforma-de-tokenizacao-de-ativos/?utm_source=thenewscc&utm_medium=email&utm_campaign=referral] e vai emitir, distribuir e negociar ativos financeiros digitalizados — basicamente, ativos tradicionais que viram representações digitais.

A nova unidade se chamará Itaú Digital Assets, marcando uma  entrada considerada inevitável pela companhia [https://www.infomoney.com.br/mercados/itau-lanca-plataforma-de-tokenizacao-de-ativos/?utm_source=thenewscc&utm_medium=email&utm_campaign=referral] no mundo de criptoativos. Ninguém vai ficar de fora.

O Ibovespa está tendo que se preocupar com muita coisa…

ECONOMIA

(GIF: Gifer | Reprodução)

As notícias de um país do tamanho do Brasil já seriam suficientes para movimentar a Bolsa, mas os temores que vêm do exterior têm prevalecido.  Nessa quinta-feira, o Ibovespa caiu 1,80%, aos 96.120 pontos, e a culpa foi externa [https://www.infomoney.com.br/mercados/ibovespa-fecha-em-queda-de-180-e-renova-minima-desde-novembro-de-2020-dolar-vai-a-r-5433/?utm_source=thenewscc&utm_medium=email&utm_campaign=referral].

Ontem, o nosso principal índice voltou a sentir o peso da inflação nos EUA — e suas perspectivas para o crescimento global — e de problemas imobiliários na China.

O movimento risk off 🔍

Esse nome é dado quando os grandes investidores não estão dispostos a tomar riscos, buscando oportunidades mais conservadoras e protegidas. Bye, bye, ações.

Para piorar as coisas, o mercado de trabalho americano demonstrou fraqueza com os  números de novos pedidos de seguro-desemprego ficando acima do esperando [https://www.infomoney.com.br/mercados/ibovespa-fecha-em-queda-de-180-e-renova-minima-desde-novembro-de-2020-dolar-vai-a-r-5433/?utm_source=thenewscc&utm_medium=email&utm_campaign=referral].

Já o dólar não sentiu tanto. A moeda americana caiu 0,07%, cotada a R$ 5,43. 💵

O que mais é bom saber no cenário econômico?

Nossa nota passou de negativa para estável.  Fitch reafirma rating BB- do Brasil e melhora perspectiva [https://www.infomoney.com.br/economia/fitch-reafirma-rating-bb-do-brasil-e-melhora-perspectiva-para-nota-de-negativa-para-estavel/?utm_source=thenewscc&utm_medium=email&utm_campaign=referral]

Acordo com o Banco Central:  Santander vai devolver R$ 79,2 milhões a clientes por cobranças indevidas [https://www.infomoney.com.br/minhas-financas/santander-vai-devolver-r-792-milhoes-a-clientes-por-cobrancas-indevidas-veja-como-receber-valores/?utm_source=thenewscc&utm_medium=email&utm_campaign=referral]

Mevo levanta R$ 45 milhões:  Investidores aportam para escalar e-commerce de medicamentos [https://braziljournal.com/mevo-atrai-investidores-para-escalar-seu-ecommerce-de-medicamentos/?utm_source=thenewscc&utm_medium=email&utm_campaign=referral]

Só invista no que tem a ver com você

PATROCINADO POR ÍON ITAÚ

Com íon, você simula quanto o seu dinheiro pode render e analisa todos os cenários. Tudo isso pra que a sua decisão seja a melhor possível na hora de investir.  Clique aqui se você quer acertar. [https://app.adjust.com/jsr?url=https%3A%2F%2Fv9v8.adj.st%2Facompanhamento-relatorios-home%3Fadj_t%3Dyb15lh7%26adj_deep_link%3Dionitau%253A%252F%252F%26adj_redirect%3Dhttps%253A%252F%252Fion.itau%252F%26adj_campaign%3Dthe_news]

O estagiário não aceita menos que 10/10

QUIZ

Somos exigentes. Informamos vocês diariamente e sabemos que vocês são espertos.  Por isso, esperamos que você acerte todas as perguntas do nosso QUIZ [http://thenewscc.com.br/quiz-atualidades]. Valendo!

Já ta sabendo que dia é hoje?

DICAS DE SEXTA

(GIF: Gifer | Reprodução)

É sexta-feira e tem dica do dênius. Se o clima de folga ainda não chegou por aí, siga as nossas dicas e aproveite o final de semana — você merece!

Ansiedade ou stress atrapalham sua alimentação? Achamos  esse produto 100% natural [http://www.satisfazvoce.com.br/] que reduz aquela “fome emocional” que faz a gente descontar tudo na comida.  Tem 15% OFF e frete grátis com o cupom SATISFAZ. [http://www.satisfazvoce.com.br/] 💪

Para quem vive recebendo a mensagem de “armazenamento quase cheio”, limpar a memória do Spotify pode solucionar o problema.  Siga a dica e libere espaço no seu celular [https://canaltech.com.br/apps/como-limpar-a-memoria-do-spotify-e-liberar-espaco-no-celular/?utm_source=email&utm_campaign=thenewscc&utm_id=referral]. 📲

Você sente que a sua vida é uma lista de tarefas infinitas? O livro  Não aguento mais não aguentar mais: Como os Millennials se tornaram a geração do burnout [https://www.amazon.com.br/N%C3%A3o-aguento-mais-n%C3%A3o-aguentar/dp/6555111976/?_encoding=UTF8&pd_rd_w=4TSBh&content-id=amzn1.sym.717e1082-1b26-481d-94d5-2a1a46904215&pf_rd_p=717e1082-1b26-481d-94d5-2a1a46904215&pf_rd_r=CY42KJN651PD1VJ61TKN&pd_rd_wg=FcFEd&pd_rd_r=4000a2e8-db85-4296-b14c-7c8210fd056e&ref_=pd_gw_ci_mcx_mr_hp_atf_m&utm_source=email&utm_campaign=thenewscc&utm_id=referral] mostra que não estamos sozinhos nessa. 📚

Quer saber como investir, ter grandes rentabilidades sem se expor tanto ao risco? Então você não pode perder  esse evento 100% online e gratuito [https://moneyweek.com.br/?referralCode=gth2b3l&refSource=copy] que acontecerá na segunda.  Inscreva-se aqui logo, as vagas vão se encerrar [https://moneyweek.com.br/?referralCode=gth2b3l&refSource=copy].💨

Saíram os indicados do Emmy 2022.  Clique para ver quem está concorrendo ao maior prêmio de televisão do mundo [https://www.omelete.com.br/series-tv/emmy-2022-indicados?utm_source=email&utm_campaign=thenewscc&utm_id=referral] — e prepare a pipoca.🍿

Campeão de audiência e sucesso garantido no brunch.  Clique para aprender a receita [https://www.panelinha.com.br/receita/Pao-Australiano?utm_source=email&utm_campaign=thenewscc&utm_id=referral] desse pão australiano — e descobrir o segredo dessa massa escura, macia e adocicada. 🥖

Quer viajar sem sair de casa?  Clique para ver os 51 melhores Airbnbs dos Estados Unidos [https://www.architecturaldigest.com/gallery/most-beautiful-airbnb-in-every-state?utm_source=email&utm_campaign=thenewscc&utm_id=referral#intcid=_architectural-digest-bottom-recirc_6474ea5e-c046-4cfa-91c2-5f2236c1b856_aff-content-entity-topic-similarity-v2] — um deleite para os olhos. 🏡

Indicações + Prêmios = FelicidadePROGRAMA DE INDICAÇÃO

O GIF é novo, mas a chance de ganhar prêmios maravilhosos segue de pé.

O trabalho que deve ser feito você já sabe. Pegue o link clicando no botão aqui em baixo, compartilhe-o com a turma e seja — muito — feliz com seus novos prêmios.

CLIQUE PARA COMPARTILHAR [https://grow.surf/x5eg0s?utm_source=newsletter&utm_medium=orgânico&utm_campaign=sessao-copy-pi]

PS: E-mails da mesma titularidade (mesmo IP) não serão considerados válidos.

the news 📬

Mais inteligente em 5 minutos. Somos um jornal gratuito e diário, que tem por objetivo te trazer tudo que você precisa saber para começar o seu dia bem e informado.

Notícias, de fato, relevantes sobre as principais atualidades do mundo, do Brasil, tecnologia e do mercado financeiro, sempre nessa ordem.

Direto na sua caixa de entrada do e-mail favorito, sempre às 06:06. É gratuito, mas pode viciar.

🎟️  O próximo anunciante pode ser você.  É só clicar aqui [https://thenewscc.typeform.com/to/twCcjR bQ].

👍👎 Gostou da edição de hoje?  Nos conte aqui [https://docs.google.com/forms/d/12jhUljBzSvd-RQKLmpXAo7tw94QchngJEi26PTrZkxg/edit].

já conhece nossas outras newsletters?

🦄  the bizness [https://thenewscc.com.br/bizness/?utm_source=newsletter&utm_medium=orgânico&utm_campaign=sessa-recomendacao]: sua dose de conteúdo sobre os assuntos mais relevantes do mundo dos negócios. análises, números e insights.  um MBA em forma de e-mail. [https://thenewscc.com.br/bizness/?utm_source=newsletter&utm_medium=orgânico&utm_campaign=sessa-recomendacao]

🏆  the champs [https://thenewscc.com.br/champs/?utm_source=newsletter&utm_medium=orgânico&utm_campaign=sessa-recomendacao]: todo o não óbvio sobre os esportes, na palma da sua mão.  descontraído e direto ao ponto, como deve ser [https://thenewscc.com.br/champs/?utm_source=newsletter&utm_medium=orgânico&utm_campaign=sessa-recomendacao].

🧸  the stories [https://thenewscc.com.br/stories/?utm_source=newsletter&utm_medium=orgânico&utm_cam paign=sessa-recomendacao]: histórias que emocionam. não tão longas quanto um romance, mas suficientes pra te fazer sentir.  contamos e escrevemos amor. [https://thenewscc.com.br/stories/?utm_source=newsletter&utm_medium=orgânico&utm_campaign=sessa-recomendacao]

até amanhã

Sempre chegamos a sua caixa de entrada por volta das 06:06. Alguns servidores de e-mail são teimosos e atrasam… Outros são piores ainda e nos jogam para o spam e/ ou promoções. Sempre que não nos encontrar na caixa de entrada, procure nessas duas.

[https://twitter.com/thenews_br]                               mais inteligente em 5 minutos.

the news.cc | newsletter

São Paulo, SP 04506-000 | Miami, FL

Política de Privacidade [https://drive.google.com/file/d/1Yi-bty-sLL5mCBwiDWKlE2JNLDclCmVe/view?usp=sharing] |  Anuncie conosco [https://thenewscc.typeform.com/to/twCcjRbQ]

Actualizar preferências https://thenews.updatemyprofile.com/t-alydytt-851105C4-jyykiytlo-td  |   Remover subscrição https://thenews.cmail19.com/t/t-u-alydytt-jyykiytlo-th/""",
        EXPECTED: [
            "relaxa.",
            "bom dia. hoje, o estagiário acordou sem inspiração e não conseguiu elaborar mensagem motivacional. às vezes, quando bate o cansaço, a única solução é um happy hour com os amigos.",
            "MUNDO",
            "Uma onda de renúncias na Europa?",
            "Boris Johnson fez escola. O primeiro-ministro italiano, Mario Draghi, formalizou ontem um pedido de renúncia do cargo, a exemplo do que seu semelhante inglês fez na semana passada.",
            "Só que o presidente do país simplesmente rejeitou o pedido e o aconselhou a se apresentar ao Parlamento, para melhor entender sua situação política.",
            "O que está acontecendo? Mario Draghi perdeu apoio do principal partido da sua base de governo, o Movimento 5 Estrelas, que boicotou uma das votações dos pacotes propostos por ele, desencadeando a crise.",
            "O boicote. O premiê propôs medidas para conter o impacto da inflação e apresentou um projeto para a construção de um incinerador de lixo. Fazendo críticas às propostas, o partido discordou do italiano.",
            "A realidade é que Draghi não precisa do apoio do partido para se manter no poder, porque tem ampla maioria no parlamento. Mas, para o político, não faz sentido ser premiê sem o apoio do M5E.",
            "A crise está instaurada na terra da pizza e a situação terá que ser bem costurada. Ao contrário do que aconteceu no Reino Unido, a maioria dos italianos quer continuar com a liderança do primeiro-ministro. Mais discreto, né? risos.",
            "O que mais é destaque mundialmente falando?",
            "Retratos da guerra. Ataques russos deixaram mais de 20 mortos no centro da Ucrânia.",
            "Conflito secreto? Israel e Irã estão desvelando várias ações clandestinas que realizam um contra o outro.",
            "Cuidado. Homem morre depois de tomar uma garrafa inteira de licor em apenas dois minutos.",
            "PECBRASIL",
            "De PEC em.",
            "Muito trabalho em Brasília. Se tem um assunto que o pessoal da política tem falado neste ano é sobre as PECs. Depois de tantos votos para mudanças na Constituição, os congressistas bateram um recorde em 2022.",
            "Este ano foi o que mais teve PECs aprovadas em toda a história da Lei Maior, nos seus longos e bem vividos 33 anos de promulgação, com 11 alterações ao texto constitucional — até agora.",
            "Looking back. O Brasil tem uma grande tradição de inovações constitucionais. O período em que houve mais mudanças foi no governo de Jair Bolsonaro, com 26, seguido pelo primeiro mandato de Dilma Rousseff, com 17.",
            "Só para comparar: Os Estados Unidos, que são conhecidos por ter uma Constituição bem enxuta, aprovou apenas 27 alterações nos seus 233 anos de existência. O Brasileiro é realmente cheio de opiniões. risos.",
            "E por falar nisso… Ontem, f oi promulgada a Emenda Constitucional Kamikaze, que autoriza o estado de emergência no país e libera um gasto público de R$ 41,2 bilhões.",
            "Outras notícias importantes no país:",
            "Polêmica no Rio Grande do Sul. Juíza eleitoral afirmou que a bandeira do Brasil seria considerada uma propaganda para o Governo Bolsonaro.",
            "Qualidade do ensino. 7 das 10 melhores universidades da América Latina estão no Brasil.",
            "Excelente para PPPs. Brasil foi eleito um dos melhores ambientes para se estabelecer parcerias público-privadas.",
            "TECNOLOGIA",
            "TikTok e Instagram estão ameaçando o Google Maps.",
            "A geração Z não gosta de mapas. Um novo estudo mostrou que 40% dos jovens não vão ao Google Maps quando procuram um lugar para almoçar — eles vão para o TikTok ou Instagram.",
            "Com a descoberta, a ameaça do aplicativo chinês aos negócios do Google não se limita apenas ao Youtube, impactando também os serviços de Pesquisa e Mapas.",
            "A explicação: O Google Maps foi feito com a intenção de levar mapas de papel para o computador. O objetivo faz sentido para quem cresceu sem GPS, mas fica distante da realidade dos adolescentes que nunca viram um mapa de papel.",
            "Segundo os executivos do Google, em vez de digitar palavras-chave, essa nova geração procura descobrir conteúdo de maneiras novas e mais imersivas.",
            "Por que isso é relevante? Embora os usuários mais velhos da Internet não usem o tico-teco para encontrar um restaurante, essa tendência pode reduzir o negócio principal do Google de pesquisa e descoberta ao longo do tempo.",
            "Tentando afastar o Google Maps dos mapas de papel, a empresa está incorporando realidade aumentada e outras inovações no sistema — será que é suficiente pra atrair a gen Z?",
            "NEGÓCIOS",
            "Enquanto a OpenSea entra no inverno cripto, o Itaú acredita no verão.",
            "Deve ser a diferença entre os hemisférios. A OpenSea — o maior mercado para negociar NFTs do mundo — parece ter visto que a febre das fotos de perfil de macacos passou e demitiu 20% de sua equipe ontem.",
            "O CEO da startup não mediu suas palavras e afirmou que a empresa entrou num inverno criptográfico sem precedentes, somado à instabilidade da economia.",
            "O medo é claro. Uma desaceleração no crescimento, depois de uma avaliação de US$ 13,3 bilhões com a corrida de alta da criptomoeda de 2021.",
            "Falando em tokens e mudando de estação…",
            "No mesmo dia das demissões da OpenSea, o Itaú anunciou que está aderindo à tokenização e vai emitir, distribuir e negociar ativos financeiros digitalizados — basicamente, ativos tradicionais que viram representações digitais.",
            "A nova unidade se chamará Itaú Digital Assets, marcando uma entrada considerada inevitável pela companhia no mundo de criptoativos. Ninguém vai ficar de fora.",
            "ECONOMIA",
            "O Ibovespa está tendo que se preocupar com muita coisa…",
            "As notícias de um país do tamanho do Brasil já seriam suficientes para movimentar a Bolsa, mas os temores que vêm do exterior têm prevalecido. Nessa quinta-feira, o Ibovespa caiu 1,80%, aos 96.120 pontos, e a culpa foi externa.",
            "Ontem, o nosso principal índice voltou a sentir o peso da inflação nos EUA — e suas perspectivas para o crescimento global — e de problemas imobiliários na China.",
            "O movimento risk off 🔍",
            "Esse nome é dado quando os grandes investidores não estão dispostos a tomar riscos, buscando oportunidades mais conservadoras e protegidas. Bye, bye, ações.",
            "Para piorar as coisas, o mercado de trabalho americano demonstrou fraqueza com os números de novos pedidos de seguro-desemprego ficando acima do esperando.",
            "Já o dólar não sentiu tanto. A moeda americana caiu 0,07%, cotada a R$ 5,43. 💵",
            "O que mais é bom saber no cenário econômico?",
            "Nossa nota passou de negativa para estável. Fitch reafirma rating BB- do Brasil e melhora perspectiva.",
            "Acordo com o Banco Central: Santander vai devolver R$ 79,2 milhões a clientes por cobranças indevidas.",
            "DICAS DE SEXTA",
            "Já ta sabendo que dia é hoje?",
            "É sexta-feira e tem dica do dênius. Se o clima de folga ainda não chegou por aí, siga as nossas dicas e aproveite o final de semana — você merece!",
            "Ansiedade ou stress atrapalham sua alimentação? Achamos esse produto 100% natural que reduz aquela “fome emocional” que faz a gente descontar tudo na comida. Tem 15% OFF e frete grátis com o cupom SATISFAZ. 💪",
            "Para quem vive recebendo a mensagem de “armazenamento quase cheio”, limpar a memória do Spotify pode solucionar o problema. Siga a dica e libere espaço no seu celular. 📲",
            "Você sente que a sua vida é uma lista de tarefas infinitas? O livro. Não aguento mais não aguentar mais: Como os Millennials se tornaram a geração do burnout mostra que não estamos sozinhos nessa. 📚",
            "Quer saber como investir, ter grandes rentabilidades sem se expor tanto ao risco? Então você não pode perder esse evento 100% online e gratuito que acontecerá na segunda. Inscreva-se aqui logo, as vagas vão se encerrar. 💨",
            "Saíram os indicados do Emmy 2022. Clique para ver quem está concorrendo ao maior prêmio de televisão do mundo — e prepare a pipoca.🍿",
            "Campeão de audiência e sucesso garantido no brunch. Clique para aprender a receita desse pão australiano — e descobrir o segredo dessa massa escura, macia e adocicada. 🥖",
            "Quer viajar sem sair de casa? Clique para ver os 51 melhores Airbnbs dos Estados Unidos — um deleite para os olhos. 🏡"
        ]
    },
    {
        ARRANGED: """keep going

bom dia. a semana está começando, mas pode ser que algum ciclo da sua vida esteja se encerrando de alguma forma. lembre-se: a cada fim, há uma chance de fazer algo novo. bola pra frente.

Chilenos dizem não à mudança constitucionalMUNDO

(Imagem: CNN Brasil | Reprodução)

Votação histórica. A população chilena foi às urnas, ontem, para decidir sobre a proposta de uma nova Constituição do país,  considerada como a maior aposta do atual governo esquerdista de lá. [https://www1.folha.uol.com.br/mundo/2022/09/chile-rejeita-nova-constituicao-por-ampla-margem-e-entra-em-periodo-de-incerteza.shtml]

Quase 62% dos mais de 11,2 milhões de eleitores  decidiram dizer não ao "novo" [https://g1.globo.com/mundo/noticia/2022/09/04/chile-rejeita-nova-constituicao-em-plebiscito-diz-imprensa-local.ghtml?utm_source=Feed+UOL&utm_medium=onebox&utm_campaign=news], demonstrando forte rejeição ao texto proposto. Mudar uma Constituição parece ser mais difícil do que o presidente Boric pensava.

Para refrescar... Os chilenos haviam decidido aposentar a Constituição atual do país em 2020, que foi escrita e promulgada há 40 anos, durante a ditadura do general  Augusto Pinochet [https://www.cnnbrasil.com.br/tudo-sobre/augusto-pinochet/].

Esquerda x Direita 🪢

Para os apoiadores, em sua maioria de esquerda, a mudança seria uma grande vitória para as minorias e significaria mais inclusão. Para a direita, seria um retrocesso político-econômico, já que o texto impõe uma maior intervenção estatal na economia.

Antes do resultado,  o presidente já havia agendado uma reunião hoje, para discussão dos próximos passos [https://www1.folha.uol.com.br/mundo/2022/09/chile-rejeita-nova-constituicao-por-ampla-margem-e-entra-em-periodo-de-incerteza.shtml]. Até lá, o povo chileno continua respeitando a Constituição anterior.

O que mais foi notícia ao redor do mundo?

Semana de decisão.  Novo primeiro-ministro britânico será decidido nesta semana, com uma série de problemas para solucionar [https://g1.globo.com/mundo/blog/sandra-cohen/post/2022/09/04/brexit-inflacao-de-dois-digitos-e-crise-energetica-entenda-o-que-espera-o-sucessor-de-boris-johnson-que-assumira-o-comando-do-governo-britanico-nesta-terca-feira.ghtml?utm_source=Feed+UOL&utm_medium=onebox&utm_campaign=news]

Tudo que vai, volta…  China promete resposta à decisão dos EUA em vender US$ 1,1 bilhão em armas para Taiwan [https://www.cnnbrasil.com.br/internacional/china-promete-resposta-a-decisao-dos-eua-de-vender-us-11-bi-em-armas-a-taiwan/?utm_source=Feed+UOL&utm_medium=onebox&utm_campaign=news]

Algo que não acontecia desde 2017:  Hamas volta a executar palestinos em Gaza [https://www.cnnbrasil.com.br/internacional/hamas-executa-cinco-palestinos-em-gaza-mortes-do-tipo-nao-aconteciam-desde-2017/?utm_source=Feed+UOL&utm_medium=onebox&utm_campaign=news]

Suspensão do pagamento do piso salarial dos enfermeirosBRASIL

(Imagem: Alves Moura | SCO)

Quem não queria ter o poder da caneta? No final de semana, o Ministro Luís Roberto Barroso suspendeu os efeitos da recém-criada Lei que estabeleceu o piso salarial da enfermagem.

Se você não se lembra... A ideia da legislação é criar o  pagamento mínimo de um valor  [https://g1.globo.com/politica/noticia/2022/08/04/bolsonaro-sanciona-projeto-que-fixa-piso-salarial-para-enfermeiros-tecnicos-auxiliares-e-parteiras.ghtml?utm_source=Feed+UOL&utm_medium=onebox&utm_campaign=news] — [https://g1.globo.com/politica/noticia/2022/08/04/bolsonaro-sanciona-projeto-que-fixa-piso-salarial-para-enfermeiros-tecnicos-auxiliares-e-parteiras.ghtml?utm_source=Feed+UOL&utm_medium=onebox&utm_campaign=news]  mais precisamente R$ 4.570  [https://g1.globo.com/politica/noticia/2022/08/04/bolsonaro-sanciona-projeto-que-fixa-piso-salarial-para-enfermeiros-tecnicos-auxiliares-e-parteiras.ghtml?utm_source=Feed+UOL&utm_medium=onebox&utm_campaign=news] — [https://g1.globo.com/politica/noticia/2022/08/04/bolsonaro-sanciona-projeto-que-fixa-piso-salarial-para-enfermeiros-tecnicos-auxiliares-e-parteiras.ghtml?utm_source=Feed+UOL&utm_medium=onebox&utm_campaign=news]  para enfermeiros [https://g1.globo.com/politica/noticia/2022/08/04/bolsonaro-sanciona-projeto-que-fixa-piso-salarial-para-enfermeiros-tecnicos-auxiliares-e-parteiras.ghtml?utm_source=Feed+UOL&utm_medium=onebox&utm_campaign=news] dos setores público e privado.

Esse valor base também iria servir de referência para outros profissionais da saúde, como técnicos e auxiliares de enfermagem, afetando todo o setor médico. É o famoso efeito dominó...

Numericamente falando:

Estima-se que a medida iria gerar um aumento dos gastos de mais de R$ 4 bilhões para municípios e de até R$ 1,3 bi para estados.

Na prática, isso poderia implicar a demissão de mais de 80 mil profissionais e o fechamento de 20 mil leitos em decorrência dessa "simples" mudança do piso salarial.

Após analisar melhor o caso, o  Ministro do STF atendeu os pedidos de entidades do setor médico  [https://www.poder360.com.br/justica/barroso-suspende-aplicacao-do-piso-salarial-da-enfermagem/?utm_source=Feed+UOL&utm_medium=onebox&utm_campaign=news/09/04/ministro-barroso-do-stf-suspende-piso-da-enfermagem.ghtml?utm_source=Feed+UOL&utm_medium=onebox&utm_campaign=news]que indicaram risco e decidiu que, para que a Lei possa valer, estados,  municípios e alguns outros interessados devem se posicionar sobre o impacto real da mudança. [https://www.poder360.com.br/justica/barroso-suspende-aplicacao-do-piso-salarial-da-enfermagem/?utm_source=Feed+UOL&utm_medium=onebox&utm_campaign=news/09/04/ministro-barroso-do-stf-suspende-piso-da-enfermagem.ghtml?utm_source=Feed+UOL&utm_medium=onebox&utm_campaign=news]

Mais notícias no cenário nacional…

O lado B do Rock in Rio.  Nos dois primeiros dias de shows, a Companhia de Limpeza Urbana já recolheu 110 toneladas de lixo [https://agenciabrasil.ebc.com.br/geral/noticia/2022-09/em-dois-dias-comlurb-recolhe-110-toneladas-de-residuos-no-rock-rio?utm_source=Feed+UOL&utm_medium=onebox&utm_campaign=news]Ele é pop mesmo…  Agronegócio emprega mais de 19 milhões de pessoas em 2022 [https://www.cnnbrasil.com.br/business/conexao-agro-agronegocio-brasileiro-emprega-mais-de-19-milhoes-em-2022/?utm_source=Feed+UOL&utm_medium=onebox&utm_campaign=news]Sobrou pra ela...  Polícia argentina prende namorada de brasileiro acusado de atacar Cristina Kirchner [https://oglobo.globo.com/mundo/noticia/2022/09/policia-argentina-prende-namorada-de-brasileiro-acusado-de-atacar-cristina-kirchner.ghtml?utm_source=globo.com&utm_medium=oglobo]                         OnlyFans já gerou quase US$ 4 bilhões aos influenciadores

OnlyFans já gerou quase US$ 4 bilhões aos influenciadoresTECNOLOGIA

(Imagem: Tube Filter | Reprodução)

Muita gente gosta do clima quente. O OnlyFans, serviço de conteúdos sexuais por assinatura, anunciou seus resultados financeiros no ano passado — e eles foram pra lá de animadores.

A receita líquida da empresa cresceu 160%, chegando a  US$ 932 milhões [https://variety.com/2022/digital/news/onlyfans-financials-earnings-creators-1235357264/?utm_source=thenewscc&utm_medium=email&utm_campaign=referral], com direito ao seu maior crescimento anual nos lucros, atingindo US$ 433 milhões. Resumindo: muito dinheiro. risos.

💰 Bem interessante. Os criadores de conteúdo do OnlyFans ganharam  US$ 3,9 bilhões em 2021 [https://variety.com/2022/digital/news/onlyfans-financials-earnings-creators-1235357264/?utm_source=thenewscc&utm_medium=email&utm_campaign=referral], um aumento de 115% em relação a 2020. A quantia depositada na conta dos criadores da plataforma sensual já se aproxima de 10 bilhões de dólares desde sua fundação, em 2016.

Crescimento para todos os lados: Assim como a receita, o número de criadores da plataforma aumentou 34% e a quantidade de usuários "sapequinhas" também seguiu esse caminho, alcançando mais de 188 milhões de contas — é quase um Brasil em fãs.

O que vem pela frente? Agora, o foco da empresa está em expandir a marca para fora dos mercados tradicionais do ocidente, já promovendo uma nova linha de negócios: seu streaming gratuito, que exclui a pornografia.

Não é à toa que tem gente copiando... Relatos internos recentes do Twitter mostraram que  a rede social pode ter planos para desenvolver seu próprio OnlyFans [https://www.theverge.com/23327809/twitter-onlyfans-child-sexual-content-problem-elon-musk], com intuito de explorar uma renda recorrente por lá.

Aprenda a andar no mundo dos investimentos!

PATROCINADO POR MONETT

Quando éramos bebês, nossos pais nos ajudaram a dar os primeiros passos. Sem alguém nos dando a mão, é mesmo difícil dar os primeiros passos…

Quando falamos de investimentos, é a mesma coisa. Sem apoio, fica mais fácil cair e se machucar. Por isso, você precisa participar da  Imersão “Como começar a investir?” [https://monett.co/cci-como-comecar-investir/?xcode=CP-NEWS-CCI-BSG-20220905-NTV-JK1-LP-JK1&utm_source=NEWS&utm_medium=NTV&utm_content=CCI&utm_campaign=CP-NEWS-CCI-BSG-20220905-NTV-JK1-LP-JK1]!

Na imersão —  100% gratuita e online [https://monett.co/cci-como-comecar-investir/?xcode=CP-NEWS-CCI-BSG-20220905-NTV-JK1-LP-JK1&utm_source=NEWS&utm_medium=NTV&utm_content=CCI&utm_campaign=CP-NEWS-CCI-BSG-20220905-NTV-JK1-LP-JK1] — você será ensinado durante 10 dias a como começar, desde dicas de boas corretoras a como fazer bons investimentos.

Serão especialistas pegando na sua mão e te ensinando a andar no universo das finanças, à disposição para te ajudar.  A oportunidade perfeita [https://monett.co/cci-como-comecar-investir/?xcode=CP-NEWS-CCI-BSG-20220905-NTV-JK1-LP-JK1&utm_source=NEWS&utm_medium=NTV&utm_content=CCI&utm_campaign=CP-NEWS-CCI-BSG-20220905-NTV-JK1-LP-JK1].

A imersão vai acontecer com Olivia Alonso [https://monett.co/cci-como-comecar-investir/?xcode=CP-NEWS-CCI-BSG-20220905-NTV-JK1-LP-JK1&utm_source=NEWS&utm_medium=NTV&utm_content=CCI&utm_campaign=CP-NEWS-CCI-BSG-20220905-NTV-JK1-LP-JK1], premiada em educação financeira, ela já vendeu mais de 30 mil livros e tem mais de 250 mil alunos!

Sempre quis investir seu dinheiro e não conseguiu por forças maiores?  Clique aqui para participar gratuitamente [https://monett.co/cci-como-comecar-investir/?xcode=CP-NEWS-CCI-BSG-20220905-NTV-JK1-LP-JK1&utm_source=NEWS&utm_medium=NTV&utm_content=CCI&utm_campaign=CP-NEWS-CCI-BSG-20220905-NTV-JK1-LP-JK1]. A imersão vai de 11 a 20 de setembro!

Amazon fecha e abandona planos para armazéns nos EUA

NEGÓCIOS

(Imagem: Rachel Jessen | Bloomberg)

Seria isso uma desaceleração? A gigante do varejo americana planeja  diminuir o tamanho da sua operação de entregas [https://www.bloomberg.com/news/articles/2022-09-02/amazon-closes-abandons-plans-for-dozens-of-us-warehouses?utm_source=thenewscc&utm_medium=email&utm_campaign=referral] em meio à redução do crescimento das vendas.

Ao que parece, a empresa fechou ou cancelou os planos de abrir 42 instalações e atrasou a abertura de mais  21 locais [https://www.bloomberg.com/news/articles/2022-09-02/amazon-closes-abandons-plans-for-dozens-of-us-warehouses?utm_source=thenewscc&utm_medium=email&utm_campaign=referral].

Na semana passada, a Amazon alertou autoridades no estado de Maryland, que planeja fechar duas estações de entrega no próximo mês, que empregam mais de 300 pessoas.

O curioso é que... 📦

O segundo semestre marca o início da temporada de compras de fim de ano. Nos anos anteriores, a maioria das empresas de e-commerce correram para abrir novas instalações e contratar mais trabalhadores.

Zoom out: Em 2020, quando as compras online dispararam, a Amazon dobrou o tamanho da sua rede de logística durante dois anos —  excedendo o Walmart. [https://www.bloomberg.com/news/articles/2022-09-02/amazon-closes-abandons-plans-for-dozens-of-us-warehouses?utm_source=thenewscc&utm_medium=email&utm_campaign=referral] Pelo visto, o pico pandêmico das compras online chegou ao fim.

Combustível fica mais barato, mas preço das passagens não cai tão cedo

ECONOMIA

(Imagem: Uselei Marcelino | Reuters)

Cenário pouco animador. No final da semana passada, a Petrobras anunciou a  redução de mais de 10% no valor do Querosene de Aviação. [https://www.infomoney.com.br/mercados/goll4-azul4-combustivel-da-aviacao-fica-mais-barato-a-partir-de-hoje-mas-nao-consegue-aliviar-custos-das-aereas/?utm_source=thenewscc&utm_medium=email&utm_campaign=referral]

Esse desconto é sobre o preço de venda para as distribuidoras e representa a segunda queda seguida no valor do combustível — que já tinha reduzido  2,6% em agosto. [https://www.infomoney.com.br/mercados/goll4-azul4-combustivel-da-aviacao-fica-mais-barato-a-partir-de-hoje-mas-nao-consegue-aliviar-custos-das-aereas/?utm_source=thenewscc&utm_medium=email&utm_campaign=referral]

O impacto nas companhias

O combustível representa 50% dos custos da Azul e Gol, por exemplo. No entanto, a redução de preço, não chega a ser um alívio sobre os gastos.

Zoom in: Entre julho de 2019, e o mesmo período de 2022, o combustível de aviação  subiu quase 170%. [https://www.infomoney.com.br/mercados/goll4-azul4-combustivel-da-aviacao-fica-mais-barato-a-partir-de-hoje-mas-nao-consegue-aliviar-custos-das-aereas/?utm_source=thenewscc&utm_medium=email&utm_campaign=referral]Nesse intervalo, o valor do diesel e da gasolina avançaram ao entorno de  125%. [https://www.infomoney.com.br/mercados/goll4-azul4-combustivel-da-aviacao-fica-mais-barato-a-partir-de-hoje-mas-nao-consegue-aliviar-custos-das-aereas/?utm_source=thenewscc&utm_medium=email&utm_campaign=referral]

Essa forte volatilidade, aliada à negociação do valor de aluguel das aeronaves da época da pandemia, dificulta a projeção de redução nos preços.

O que acontecerá nesta semana? 📅

CALENDÁRIO DA SEMANA

🏢 Labor Day: Hoje, as bolsas dos EUA estão fechadas em função do Dia do Trabalho.

🇪🇺 Reunião do Banco Central Europeu: Na agenda internacional, a semana está cheia. O momento mais   aguardado é a reunião do BCE,  que decidirá sobre a taxa de juros do bloco europeu [https://www.infomoney.com.br/mercados/ipca-de-agosto-reuniao-do-banco-central-e-europeu-e-conversa-com-jerome-powell-o-que-acompanhar-na-semana/?utm_source=thenewscc&utm_medium=email&utm_campaign=referral]. A previsão é de uma alta de 0,75 ponto percentual.

🇧🇷 Dia da Independência: Por aqui, na quarta-feira,  teremos um feriado que promete ser movimentad  o [https://www.infomoney.com.br/mercados/ipca-de-agosto-reuniao-do-banco-central-e-europeu-e-conversa-com-jerome-powell-o-que-acompanhar-na-semana/?utm_source=thenewscc&utm_medium=email&utm_campaign=referral]. Nosso 7 de Setembro será marcado por manifestações políticas, esperadas e planejadas já há algum tempo.

🇺🇸 Jerome Powell: O presidente do Federal Reserve participará, nesta semana, de um evento que será   transmitido ao vivo e promete atrair muita atenção.  Será a primeira fala de Powell depois de Jackson Hole [https://www.infomoney.com.br/mercados/ipca-de-agosto-reuniao-do-banco-central-e-europeu-e-conversa-com-jerome-powell-o-que-acompanhar-na-semana/?utm_source=thenewscc&utm_medium=email&utm_campaign=referral]. Stay tunned.

📊 IPCA: Na sexta-feira, será divulgado o Índice de Preços ao Consumidor Amplo referente a agosto,  um importante indicador da inflação [https://www.infomoney.com.br/mercados/ipca-de-agosto-reuniao-do-banco-central-e-europeu-e-conversa-com-jerome-powell-o-que-acompanhar-na-semana/?utm_source=thenewscc&utm_medium=email&utm_campaign=referral]. A média da projeção dos economistas é de uma deflação — a segunda seguida — de 0,39%.

SegundinhaPROGRAMA DE INDICAÇÃO

Toda segunda feira traz uma nova chance. Use o dia de hoje para guiar o resto da semana, e fazer dela a melhor de todas.

Pensando nisso, que tal utilizar uma parte do seu tempo para conquistar prêmios?

Aqui no the news, funciona assim. Você faz uma boa ação, deixando seus amigos bem e informados, e ainda é recompensado por isso.

Clique no botãozinho amarelo aqui em baixo, pegue o seu link e espalhe por toda a internet. Em troca das indicações, o estagiário te da prêmios.

CLIQUE PARA COMPARTILHAR [https://grow.surf/x5eg0s?utm_source=newsletter&utm_medium=orgânico&utm_campaign=sessao-copy-pi]

PS: E-mails da mesma titularidade (mesmo IP) não serão considerados válidos.

the news 📬

Mais inteligente em 5 minutos. Somos um jornal gratuito e diário, que tem por objetivo te trazer tudo que você precisa saber para começar o seu dia bem e informado.

Notícias, de fato, relevantes sobre as principais atualidades do mundo, do Brasil, tecnologia e do mercado financeiro, sempre nessa ordem.

Direto na sua caixa de entrada do e-mail favorito, sempre às 06:06. É gratuito, mas pode viciar.

🎟️  O próximo anunciante pode ser você.  É só clicar aqui [https://thenewscc.typeform.com/to/twCcjR bQ].

👍👎 Gostou da edição de hoje?  Nos conte aqui [https://docs.google.com/forms/d/12jhUljBzSvd-RQKLmpXAo7tw94QchngJEi26PTrZkxg/edit].

já conhece nossas outras newsletters?

🦄  the bizness [https://thenewscc.com.br/bizness/?utm_source=newsletter&utm_medium=orgânico&utm_campaign=sessa-recomendacao]: sua dose de conteúdo sobre os assuntos mais relevantes do mundo dos negócios. análises, números e insights.  um MBA em forma de e-mail. [https://thenewscc.com.br/bizness/?utm_source=newsletter&utm_medium=orgânico&utm_campaign=sessa-recomendacao]

🏆  the champs [https://thenewscc.com.br/champs/?utm_source=newsletter&utm_medium=orgânico&utm_campaign=sessa-recomendacao]: todo o não óbvio sobre os esportes, na palma da sua mão.  descontraído e direto ao ponto, como deve ser [https://thenewscc.com.br/champs/?utm_source=newsletter&utm_medium=orgânico&utm_campaign=sessa-recomendacao].

🧸  the stories [https://thenewscc.com.br/stories/?utm_source=newsletter&utm_medium=orgânico&utm_cam paign=sessa-recomendacao]: histórias que emocionam. não tão longas quanto um romance, mas suficientes pra te fazer sentir.  contamos e escrevemos amor. [https://thenewscc.com.br/stories/?utm_source=newsletter&utm_medium=orgânico&utm_campaign=sessa-recomendacao]

até amanhã

Sempre chegamos a sua caixa de entrada por volta das 06:06. Alguns servidores de e-mail são teimosos e atrasam… Outros são piores ainda e nos jogam para o spam e/ ou promoções. Sempre que não nos encontrar na caixa de entrada, procure nessas duas.

[https://twitter.com/thenews_br]                               mais inteligente em 5 minutos.

the news.cc | newsletter

São Paulo, SP 04506-000 | Miami, FL

Política de Privacidade [https://drive.google.com/file/d/1Yi-bty-sLL5mCBwiDWKlE2JNLDclCmVe/view?usp=sharing] |  Anuncie conosco [https://thenewscc.typeform.com/to/twCcjRbQ]

Actualizar preferências https://thenews.updatemyprofile.com/t-ajkurdk-AF625213-ykhdduoju-td  |   Remover subscrição https://thenews.cmail20.com/t/t-u-ajkurdk-ykhdduoju-th/
""",
        EXPECTED: [
            "keep going.",
            "bom dia. a semana está começando, mas pode ser que algum ciclo da sua vida esteja se encerrando de alguma forma. lembre-se: a cada fim, há uma chance de fazer algo novo. bola pra frente.",
            "MUNDO",
            "Chilenos dizem não à mudança constitucional.",
            "Votação histórica. A população chilena foi às urnas, ontem, para decidir sobre a proposta de uma nova Constituição do país, considerada como a maior aposta do atual governo esquerdista de lá.",
            "Quase 62% dos mais de 11,2 milhões de eleitores decidiram dizer não ao 'novo', demonstrando forte rejeição ao texto proposto. Mudar uma Constituição parece ser mais difícil do que o presidente Boric pensava.",
            "Para refrescar… Os chilenos haviam decidido aposentar a Constituição atual do país em 2020, que foi escrita e promulgada há 40 anos, durante a ditadura do general. Augusto Pinochet.",
            "Esquerda x Direita 🪢",
            "Para os apoiadores, em sua maioria de esquerda, a mudança seria uma grande vitória para as minorias e significaria mais inclusão. Para a direita, seria um retrocesso político-econômico, já que o texto impõe uma maior intervenção estatal na economia.",
            "Antes do resultado, o presidente já havia agendado uma reunião hoje, para discussão dos próximos passos. Até lá, o povo chileno continua respeitando a Constituição anterior.",
            "O que mais foi notícia ao redor do mundo?",
            "Semana de decisão. Novo primeiro-ministro britânico será decidido nesta semana, com uma série de problemas para solucionar.",
            "Tudo que vai, volta… China promete resposta à decisão dos EUA em vender US$ 1,1 bilhão em armas para Taiwan.",
            "Algo que não acontecia desde 2017: Hamas volta a executar palestinos em Gaza.",
            "BRASIL",
            "Suspensão do pagamento do piso salarial dos enfermeiros.",
            "Quem não queria ter o poder da caneta? No final de semana, o Ministro Luís Roberto Barroso suspendeu os efeitos da recém-criada Lei que estabeleceu o piso salarial da enfermagem.",
            "Se você não se lembra… A ideia da legislação é criar o pagamento mínimo de um valor — mais precisamente R$ 4.570 — para enfermeiros dos setores público e privado.",
            "Esse valor base também iria servir de referência para outros profissionais da saúde, como técnicos e auxiliares de enfermagem, afetando todo o setor médico. É o famoso efeito dominó…",
            "Numericamente falando:",
            "Estima-se que a medida iria gerar um aumento dos gastos de mais de R$ 4 bilhões para municípios e de até R$ 1,3 bi para estados.",
            "Na prática, isso poderia implicar a demissão de mais de 80 mil profissionais e o fechamento de 20 mil leitos em decorrência dessa 'simples' mudança do piso salarial.",
            "Após analisar melhor o caso, o Ministro do STF atendeu os pedidos de entidades do setor médico que indicaram risco e decidiu que:",
            "para que a Lei possa valer, estados, municípios e alguns outros interessados devem se posicionar sobre o impacto real da mudança.",
            "Mais notícias no cenário nacional…",
            "O lado B do Rock in Rio.",
            "Nos dois primeiros dias de shows, a Companhia de Limpeza Urbana já recolheu 110 toneladas de lixo.",
            "Ele é pop mesmo… Agronegócio emprega mais de 19 milhões de pessoas em 2022.",
            "Sobrou pra ela… Polícia argentina prende namorada de brasileiro acusado de atacar Cristina Kirchner.",
            "OnlyFans já gerou quase US$ 4 bilhões aos influenciadores.",
            "TECNOLOGIA",
            "OnlyFans já gerou quase US$ 4 bilhões aos influenciadores.",
            "Muita gente gosta do clima quente. O OnlyFans, serviço de conteúdos sexuais por assinatura, anunciou seus resultados financeiros no ano passado — e eles foram pra lá de animadores.",
            "A receita líquida da empresa cresceu 160%, chegando a US$ 932 milhões, com direito ao seu maior crescimento anual nos lucros, atingindo US$ 433 milhões. Resumindo: muito dinheiro. risos.",
            "💰 Bem interessante.",
            "Os criadores de conteúdo do OnlyFans ganharam.",
            "US$ 3,9 bilhões em 2021, um aumento de 115% em relação a 2020.",
            "A quantia depositada na conta dos criadores da plataforma sensual já se aproxima de 10 bilhões de dólares desde sua fundação, em 2016.",
            "Crescimento para todos os lados: Assim como a receita, o número de criadores da plataforma aumentou 34% e a quantidade de usuários 'sapequinhas' também seguiu esse caminho, alcançando mais de 188 milhões de contas — é quase um Brasil em fãs.",
            "O que vem pela frente? Agora, o foco da empresa está em expandir a marca para fora dos mercados tradicionais do ocidente, já promovendo uma nova linha de negócios: seu streaming gratuito, que exclui a pornografia.",
            "Não é à toa que tem gente copiando… Relatos internos recentes do Twitter mostraram que a rede social pode ter planos para desenvolver seu próprio OnlyFans, com intuito de explorar uma renda recorrente por lá.",
            "NEGÓCIOS",
            "Amazon fecha e abandona planos para armazéns nos EUA.",
            "Seria isso uma desaceleração? A gigante do varejo americana planeja diminuir o tamanho da sua operação de entregas em meio à redução do crescimento das vendas.",
            "Ao que parece, a empresa fechou ou cancelou os planos de abrir 42 instalações e atrasou a abertura de mais 21 locais.",
            "Na semana passada, a Amazon alertou autoridades no estado de Maryland, que planeja fechar duas estações de entrega no próximo mês, que empregam mais de 300 pessoas.",
            "O curioso é que… 📦",
            "O segundo semestre marca o início da temporada de compras de fim de ano. Nos anos anteriores, a maioria das empresas de e-commerce correram para abrir novas instalações e contratar mais trabalhadores.",
            "Zoom out: Em 2020, quando as compras online dispararam, a Amazon dobrou o tamanho da sua rede de logística durante dois anos — excedendo o Walmart. Pelo visto, o pico pandêmico das compras online chegou ao fim.",
            "ECONOMIA",
            "Combustível fica mais barato, mas preço das passagens não cai tão cedo.",
            "Cenário pouco animador. No final da semana passada, a Petrobras anunciou a redução de mais de 10% no valor do Querosene de Aviação.",
            "Esse desconto é sobre o preço de venda para as distribuidoras e representa a segunda queda seguida no valor do combustível — que já tinha reduzido 2,6% em agosto.",
            "O impacto nas companhias.",
            "O combustível representa 50% dos custos da Azul e Gol, por exemplo. No entanto, a redução de preço, não chega a ser um alívio sobre os gastos.",
            "Zoom in: Entre julho de 2019, e o mesmo período de 2022, o combustível de aviação subiu quase 170%. Nesse intervalo, o valor do diesel e da gasolina avançaram ao entorno de 125%.",
            "Essa forte volatilidade, aliada à negociação do valor de aluguel das aeronaves da época da pandemia, dificulta a projeção de redução nos preços.",
            "CALENDÁRIO DA SEMANA",
            "O que acontecerá nesta semana? 📅",
            "🏢 Labor Day: Hoje, as bolsas dos EUA estão fechadas em função do Dia do Trabalho.",
            "🇪🇺 Reunião do Banco Central Europeu: Na agenda internacional, a semana está cheia. O momento mais aguardado é a reunião do BCE, que decidirá sobre a taxa de juros do bloco europeu. A previsão é de uma alta de 0,75 ponto percentual.",
            "🇧🇷 Dia da Independência: Por aqui, na quarta-feira, teremos um feriado que promete ser movimentad o. Nosso 7 de Setembro será marcado por manifestações políticas, esperadas e planejadas já há algum tempo.",
            "🇺🇸 Jerome Powell: O presidente do Federal Reserve participará, nesta semana, de um evento que será transmitido ao vivo e promete atrair muita atenção. Será a primeira fala de Powell depois de Jackson Hole. Stay tunned.",
            "📊 IPCA: Na sexta-feira, será divulgado o Índice de Preços ao Consumidor Amplo referente a agosto, um importante indicador da inflação. A média da projeção dos economistas é de uma deflação — a segunda seguida — de 0,39%."
        ]
    },
    {
        ARRANGED: '''
    é hora de escolher

bom dia. a parte difícil do foco não é dizer "sim" para o seu objetivo, mas conseguir falar "não" às várias outras possibilidades que existem. escolha com carinho.

Rússia fez maior ataque aéreo na Ucrânia desde o início da guerraMUNDO

(Imagem: Reuters | Reprodução)

Alerta em Kiev. Ontem, depois de três meses sem ataques, a capital da Ucrânia foi fortemente bombardeada pela Rússia. Até o momento,  14 civis [https://www.cnnbrasil.com.br/internacional/kiev-lviv-e-outras-cidades-ucranianas-sao-atingidas-por-explosoes/?utm_source=thenewscc&utm_medium=email&utm_campaign=referral] morreram e  97 ficaram feridos. [https://www.cnnbrasil.com.br/internacional/kiev-lviv-e-outras-cidades-ucranianas-sao-atingidas-por-explosoes/?utm_source=thenewscc&utm_medium=email&utm_campaign=referral]

Os principais alvos foram instalações de energia, comando militar e comunicação. Outras cidades do país também foram atacadas, o que pode indicar uma nova fase da guerra.

Qual o motivo do ataque? De acordo com as falas de Putin, os mísseis são uma resposta ao bombardeio na  ponte entre Rússia e Crimeia no sábado. [https://thenewscc.com.br/2022/10/10/explosao-derruba-ponte-que-liga-russia-a-crimeia/?dxp_referrer=https%3A%2F%2Fwww.google.com%2F&utm_source=thenewscc&utm_medium=email&utm_campaign=referral] Essa ação, inclusive, foi classificada pelo presidente russo como “ato de terrorismo internacional”.

Contextualizando… Por conta da forte resistência ucraniana no primeiro semestre, a Rússia suspendeu os ataques na capital e focou seus esforços no leste e sul do país —  territórios que foram anexados  [https://exame.com/mundo/russia-oficializa-anexacao-de-territorio-da-ucrania/?utm_source=thenewscc&utm_medium=email&utm_campaign=referral] no último mês [https://exame.com/mundo/russia-oficializa-anexacao-de-territorio-da-ucrania/?utm_source=thenewscc&utm_medium=email&utm_campaign=referral].

🇺🇸 Depois dos ataques de ontem, Joe Biden garantiu apoio contínuo dos EUA à Ucrânia. Nas palavras   do presidente americano,  a cooperação militar entre os dois países será prioridade [https://www.cnnbrasil.com.br/internacional/biden-promete-sistemas-de-defesa-aerea-para-a-ucrania-apos-ataque-com-misseis/?utm_source=thenewscc&utm_medium=email&utm_campaign=referral].

What's next? O Ministro das Relações Exteriores da Ucrânia anunciou que o país vai continuar com  ações ofensivas contra novos ataques russos [https://www.cnnbrasil.com.br/live-update/internacional/as-ultimas-noticias-da-guerra-na-ucrania-2/1978503/?utm_source=thenewscc&utm_medium=email&utm_campaign=referral]. A guerra muda de fase, mas a tensão continua a mesma...

O que mais foi notícia ao redor do globo?

"Dia Mundial contra a Pena Capital".  Papa Francisco pede fim da pena de morte [https://g1.globo.com/mundo/noticia/2022/10/10/papa-francisco-pede-fim-da-pena-de-morte.ghtml?utm_source=thenewscc&utm_medium=email&utm_campaign=referral]Tribunal francês:  Começou o julgamento da Air France e Airbus sobre o acidente com o voo que ia do Rio a Paris em 2009 [https://g1.globo.com/mundo/noticia/2022/10/10/comeca-julgamento-da-air-france-e-airbus-sobre-o-acidente-com-voo-af447-que-ia-de-rio-a-paris-em-2009.ghtml?utm_source=thenewscc&utm_medium=email&utm_campaign=referral]Vítimas tropicais.  A tempestade Julia deixa 14 mortos na América Central e segue para o México [https://g1.globo.com/mundo/noticia/2022/10/10/tempestade-julia-deixa-14-mortos-na-america-central-e-segue-para-o-mexico.ghtml?utm_source=thenewscc&utm_medium=email&utm_campaign=referral]                 Candidatos gastaram milhões em marketing na internet

BRASIL

(Ilustração | the news)

O TSE divulgou que os candidatos às Eleições Gerais de 2022 já gastaram mais de  R$ 196 milhões [https://divulgacandcontas.tse.jus.br/divulga/?utm_source=thenewscc&utm_medium=email&utm_campaign=referral#/consulta/campanha/2022/2040602022/ranks] promovendo seus conteúdos na internet.

Se for feita uma comparação com 2018, a soma do investimento total gasto nas propagandas on-line chegou a R$ 99,7 milhões, ou seja, esse número quase dobrou agora.

A eleição deste ano está mostrando que não tem mais como fazer uma campanha sem considerar tráfego pago nas redes. E parece que os candidatos entenderam isso.

Falando só dos presidenciáveis… Entre aqueles que lideraram as intenções de voto, Simone Tebet (MDB) foi a que mais investiu em tráfego para impulsionar os seus conteúdos —  ao todo foram R$ 2,7 milhões. [https://www.jota.info/eleicoes/gastos-dos-candidatos-a-presidencia-revelam-estrategias-para-alcancar-eleitores-23092022?utm_source=thenewscc&utm_medium=email&utm_campaign=referral]

Logo atrás está o Lula (PT), que gastou  R$ 2,5 milhões [https://www.jota.info/eleicoes/gastos-dos-candidatos-a-presidencia-revelam-estrategias-para-alcancar-eleitores-23092022?utm_source=thenewscc&utm_medium=email&utm_campaign=referral], depois Ciro do PDT, com o valor de  R$ 1,6 milhão [https://www.jota.info/eleicoes/gastos-dos-candidatos-a-presidencia-revelam-estrategias-para-alcancar-eleitores-23092022?utm_source=thenewscc&utm_medium=email&utm_campaign=referral] e, em último, Bolsonaro (PL), que gastou em torno de  R$ 530 mil. [https://www.jota.info/eleicoes/gastos-dos-candidatos-a-presidencia-revelam-estrategias-para-alcancar-eleitores-23092022?utm_source=thenewscc&utm_medium=email&utm_campaign=referral]

Gás final. Na última semana antes do primeiro turno, a plataforma de anúncios do Google recebeu vários acordos de prestação de serviço. Foram investidos mais  R$ 700 mil em quatro horas no Google [https://olhardigital.com.br/2022/09/28/internet-e-redes-sociais/eleicoes-de-2022-candidatos-gastaram-mais-de-r-147-milhoes-em-marketing-na-internet/?utm_source=thenewscc&utm_medium=email&utm_campaign=referral].

Bottom-line: As despesas com propagandas eleitorais na TV e no rádio estão diminuindo cada vez mais. No primeiro turno, foram registrados  quase R$ 400 milhões, [https://divulgacandcontas.tse.jus.br/divulga/?utm_source=thenewscc&utm_medium=email&utm_campaign=referral#/consulta/campanha/2022/2040602022/ranks] 15% a menos do que em 2018.

Outras notícias relevantes no Brasil:

Ex-presidente:  STF marca julgamento de ação contra Collor na Lava Jato [https://www.poder360.com.br/justica/stf-marca-julgamento-de-acao-contra-collor-na-lava-jato/?utm_source=thenewscc&utm_medium=email&utm_campaign=referral]Atrasos na pista…  Aeroporto de Congonhas tem 300 voos cancelados depois que um avião teve o pneu furado durante o pouso [https://www.poder360.com.br/brasil/congonhas-tem-283-voos-cancelados-diz-infraero/?utm_source=thenewscc&utm_medium=email&utm_campaign=referral]Acordos.  Brasil passa a vender energia excedente para Argentina e Uruguai [https://www.cnnbrasil.com.br/business/brasil-passa-a-vender-energia-excedente-para-argentina-e-uruguai/?utm_source=thenewscc&utm_medium=email&utm_campaign=referral]                 As marcas estão investindo em músicas virais do TikTok

TECNOLOGIA

(GIF: Tenor | Reprodução)

Marketing de ouvido. Recentemente, algumas empresas começaram a desenvolver sons originais do TikTok, na esperança de bombarem e se tornarem virais no aplicativo chinês.

Para as marcas, um som "chiclete" oferece visibilidade e uma probabilidade maior de alcançar as páginas “For you” de mais usuários.

Explicando… Quando um criador carrega um vídeo no TikTok com som original, outros usuários podem usar o mesmo som para criar vídeos próprios. À medida que mais pessoas usam o som original, ele vai se tornando viral.

Como o algoritmo “empurra” o que está funcionando, esses sons acabam impulsionando conteúdos. Só pra ter ideia,  “As It Was” de Harry Styles [https://www.tiktok.com/@hshq/video/7084673462417100074?is_from_webapp=v1&item_id=7084673462417100074&utm_source=thenewscc&utm_medium=email&utm_campaign=referral] e  “Vibe” de Cookiee Kawaii [https://www.tiktok.com/@qpark/video/6798581473222905094?is_from_webapp=v1&item_id=6798581473222905094&utm_source=thenewscc&utm_medium=email&utm_campaign=referral], foram usados em quase 4 milhões de vídeos.

O que está acontecendo agora?

As marcas estão querendo entrar no jogo, mas, por problemas de licenciamento, nem sempre têm acesso aos hits. Assim, para navegar pelas legalidades, os varejistas começaram a fazer parcerias com artistas e lançar desafios no TikTok.

A Pepsi anunciou uma parceria com a cantora e atriz Chlöe Bailey, na terça-feira, para lançar uma nova versão da música  “Footloose” [https://www.youtube.com/watch?v=z_DZLRtCxv0&utm_source=thenewscc&utm_medium=email&utm_campaign=referral];A American Eagle e a cantora do TikTok, Katherine Li, se uniram para criar uma versão personalizada de sua música  “Happening Again” [https://www.youtube.com/watch?v=_9Coduep9Es&utm_source=thenewscc&utm_medium=email&utm_campaign=referral];A Pizza Hut colaborou com Jon Moss, um TikToker com quase 7 milhões de seguidores, para criar um  hino que celebrasse o retorno da Detroit-Style Pizza [https://open.spotify.com/track/2kdATWV9eSlKtzI50oRLkK?si=b86960f8cc884545&nd=1&utm_source=thenewscc&utm_medium=email&utm_campaign=referral#login].

Zoom Out: Os varejistas vêm criando jingles na televisão e no rádio há décadas, porém, agora, o desafio é diferente. Além de se ajustarem ao vídeo curto e na vertical, as marcas estão tentando usar o algoritmo — imprevisível — ao seu favor.

A Heineken® 0.0 te levará às mais altas velocidades

PATROCINADO POR HEINEKEN® 0.0

Você é rápido o suficiente? A Heineken® 0.0, patrocinadora global da F1, convida os fãs de games e automobilismo para participarem do torneio em busca do Player 0.0: o competidor mais rápido do Brasil no jogo  Fórmula 1 2022. [https://player00.heineken.com.br/?utm_source=the_news&utm_medium=e-mail&utm_campaign=11_10&utm_id=thenewscc&utm_term=broad-default-the_news-banner&utm_content=novo_freemium-performance-instalacoes_de_app_aaa-broad-default-the_news-29_de_agosto_2022-gif-banner-null]

O evento unirá gamers, pilotos e consumidores em uma experiência única —  daquelas que só a Heineken® proporciona. [https://player00.heineken.com.br/?utm_source=the_news&utm_medium=e-mail&utm_campaign=11_10&utm_id=thenewscc&utm_term=broad-default-the_news-banner&utm_content=novo_freemium-performance-instalacoes_de_app_aaa-broad-default-the_news-29_de_agosto_2022-gif-banner-null]

The best: Você pode participar gratuitamente, ser o mais rápido e, caso vá para as finais, conhecer Interlagos diretamente do  Heineken Village [https://player00.heineken.com.br/?utm_source=the_news&utm_medium=e-mail&utm_campaign=11_10&utm_id=thenewscc&utm_term=broad-default-the_news-banner&utm_content=novo_freemium-performance-instalacoes_de_app_aaa-broad-default-the_news-29_de_agosto_2022-gif-banner-null], espaço inédito dentro do autódromo!

Quem está envolvido? 💚🍺

Nada mais nada menos que os maiores streamers da atualidade —  Gaules , Ale Apoka, Velho Vamp e Victor Ludgero [https://player00.heineken.com.br/?utm_source=the_news&utm_medium=e-mail&utm_campaign=11_10&utm_id=thenewscc&utm_term=broad-default-the_news-banner&utm_content=novo_freemium-performance-instalacoes_de_app_aaa-broad-default-the_news-29_de_agosto_2022-gif-banner-null], são alguns dos grandes nomes que irão narrar as últimas etapas do campeonato.

Para participar é simples, 100% grátis e a primeira etapa é totalmente online. Basta ter mais de 25 anos, adrenalina no sangue e preencher esse formulário  aqui. [https://player00.heineken.com.br/?utm_source=the_news&utm_medium=e-mail&utm_campaign=11_10&utm_id=thenewscc&utm_term=broad-default-the_news-banner&utm_content=novo_freemium-performance-instalacoes_de_app_aaa-broad-default-the_news-29_de_agosto_2022-gif-banner-null]

Se você já está convencido de que é um piloto veloz, a dica é simples, não seja lento na hora de garantir sua vaga.  As inscrições são grátis porém limitadas e estarão abertas de hoje até o dia 15 deste mês. [https://player00.heineken.com.br/?utm_source=the_news&utm_medium=e-mail&utm_campaign=11_10&utm_id=thenewscc&utm_term=broad-default-the_news-banner&utm_content=novo_freemium-performance-instalacoes_de_app_aaa-broad-default-the_news-29_de_agosto_2022-gif-banner-null] LIGHTS OUT AND AWAY WE GO!

Amazon vai gastar 1 bilhão de euros com veículos elétricos

NEGÓCIOS

(Imagem: Reuters | Reprodução)

Rumo ao carbono líquido zero. A Amazon anunciou, ontem, que gastará 1 bilhão de euros para eletrificar sua frota na Europa. O dinheiro será usado para  dobrar o número de veículos elétricos [https://www.businessinsider.com/amazon-plans-10000-electric-delivery-vans-europe-2025-2022-10?utm_source=thenewscc&utm_medium=email&utm_campaign=referral] no continente.

Segundo a empresa, o investimento acelerará a inovação no setor de transporte como um todo e contribuirá para o desenvolvimento da  infraestrutura de recarga de veículos [https://www.reuters.com/business/autos-transportation/amazoncom-invest-over-1-bln-euros-european-electric-van-truck-fleet-2022-10-09/?utm_source=thenewscc&utm_medium=email&utm_campaign=referral].

Contexto: O anúncio ocorre depois da divulgação do relatório de sustentabilidade da empresa. Apesar dos esforços para se vender como  líder em ação climática [https://www.theverge.com/2022/10/10/23396499/amazon-electric-delivery-vehicle-europe-investment?utm_source=thenewscc&utm_medium=email&utm_campaign=referral], suas emissões de dióxido de carbono cresceram 18% no último ano.

Nas palavras do CEO da Amazon, “a rede de transporte é uma das áreas mais desafiadoras do negócio para descarbonizar, e para alcançar o carbono líquido zero será necessário um investimento substancial e sustentável”.

O mercado está de olho… 👀

Embora muitas empresas de logística,  incluindo gigantes como UPS e FedEx [https://avalanchenoticias.com.br/carros-motos-veiculos/amazon-investe-mais-de-1-bilhao-de-euros-para-expandir-sua-frota-de-vans-e-caminhoes-eletricos-na-europa/?utm_source=thenewscc&utm_medium=email&utm_campaign=referral], tenham prometido comprar mais veículos elétricos de emissão zero, ainda não há muitas vans e caminhões à venda.

Percebendo o movimento, várias startups estão correndo para suprir essa demanda do mercado. Da mesma forma, fabricantes maiores —  General Motors, Volkswagen, Ford e Tesla [https://www.reuters.com/business/autos-transportation/amazoncom-invest-over-1-bln-euros-european-electric-van-truck-fleet-2022-10-09/?utm_source=thenewscc&utm_medium=email&utm_campaign=referral] — também passaram a focar nos veículos elétricos para entregas.

O que ir na academia tem em comum com a sua vida financeira?

PATROCINADO POR TC

Seja queimando calorias ou investindo, os resultados não costumam aparecer da noite para o dia. Mas com tempo e uma rotina focada, a magia acontece. ✨

Para ter sucesso nos investimentos, o mais importante é começar. Não sabe como? O TC pode te ajudar.  Uma plataforma completa — e grátis — para investidores. [https://tradersclub.onelink.me/hjLz/0gfmk0j0?utm_source=the_news&utm_medium=e-mail&utm_campaign=11_10&utm_id=thenewscc&utm_term=broad-default-the_news-banner&utm_content=novo_freemium-performance-instalacoes_de_app_aaa-broad-default-the_news-29_de_agosto_2022-gif-banner-null]

O aplicativo oferece  todas as ferramentas úteis [https://tradersclub.onelink.me/hjLz/0gfmk0j0?utm_source=the_news&utm_medium=e-mail&utm_campaign=11_10&utm_id=thenewscc&utm_term=broad-default-the_news-banner&utm_content=novo_freemium-performance-instalacoes_de_app_aaa-broad-default-the_news-29_de_agosto_2022-gif-banner-null] para você ir mais rápido e mais longe nos investimentos.

Quer exemplos?

No TC, você tem notícias e informações em tempo real, pode conferir cotações, sincronizar ativos e acompanhar sua carteira…  Inclusive, consegue até ver no que especialistas estão investindo. [https://tradersclub.onelink.me/hjLz/0gfmk0j0?utm_source=the_news&utm_medium=e-mail&utm_campaign=11_10&utm_id=thenewscc&utm_term=broad-default-the_news-banner&utm_content=novo_freemium-performance-instalacoes_de_app_aaa-broad-default-the_news-29_de_agosto_2022-gif-banner-null] 👀

É quase como ter um personal trainer, só que nas finanças.  Clique aqui para abrir uma conta grátis no TC e comece ainda hoje! [https://tradersclub.onelink.me/hjLz/0gfmk0j0?utm_source=the_news&utm_medium=e-mail&utm_campaign=11_10&utm_id=thenewscc&utm_term=broad-default-the_news-banner&utm_content=novo_freemium-performance-instalacoes_de_app_aaa-broad-default-the_news-29_de_agosto_2022-gif-banner-null]

Real foi a 8ª moeda que mais se valorizou em 2022

ECONOMIA

(Imagem: Pixabay | Reprodução)

Segundo levantamento, o real foi a  8ª moeda que mais valorizou em relação ao dólar [https://www.poder360.com.br/economia/real-foi-a-8a-moeda-que-mais-se-valorizou-em-2022/?utm_source=thenewscc&utm_medium=email&utm_campaign=referral] americano em 2022. Desde o início do ano, a nossa moeda subiu 6,9%.

Entre as principais economias mundiais, a moeda brasileira só valorizou menos do que a da Rússia, que já  subiu 18,7% no mesmo período [https://noticias.uol.com.br/internacional/ultimas-noticias/2022/10/08/imagens-ponte-crimeia-antes-e-depois-da-explosao.htm?utm_source=thenewscc&utm_medium=email&utm_campaign=referral].

📈 Ainda nos destaques positivos, o kwanza da Angola foi a moeda que teve maior alta,  subindo 29,7% [https://br.noticias.yahoo.com/real-foi-a-8-moeda-que-mais-se-valorizou-em-2022-diz-levantamento-155430449.html?utm_source=thenewscc&utm_medium=email&utm_campaign=referral]. Logo em seguida, ficaram o rublo russo e o dram da Armênia.

📉 Na América do Sul, o pior desempenho foi da Venezuela, que viu sua moeda se desvalorizar 44%. Mas  o pior desempenho do ano [https://br.noticias.yahoo.com/real-foi-a-8-moeda-que-mais-se-valorizou-em-2022-diz-levantamento-155430449.html?utm_source=thenewscc&utm_medium=email&utm_campaign=referral] foi o da rúpia do Sri Lanka, fechando em 45%.

O levantamento se baseou em 118 países e na zona do euro, que desvalorizou quase 14% neste ano.  Se quiser ver o relatório na íntegra, é só clicar aqui [https://static.poder360.com.br/2022/10/ranking-moedas-valorizacao-dolar-7out2022.pdf?utm_source=thenewscc&utm_medium=email&utm_campaign=referral].

Destaques do dia:

Fechamento:  Ibovespa cai 0,37%, acompanhando pares internacionais em sessão de cautela; dólar cai 0,42% [https://www.infomoney.com.br/mercados/ibovespa-cai-037-acompanhando-pares-internacionais-em-sessao-de-cautela-dolar-cai-042/?utm_source=thenewscc&utm_medium=email&utm_campaign=referral]As contas estão apertando...  Endividamento atinge 80% das famílias mais pobres em setembro [https://www.cnnbrasil.com.br/business/endividamento-atinge-80-das-familias-mais-pobres-em-setembro-um-recorde-diz-cnc/?utm_source=thenewscc&utm_medium=email&utm_campaign=referral]Recuperação da indústria.  Produção de veículos tem alta de 19,3% em setembro [https://agenciabrasil.ebc.com.br/economia/noticia/2022-10/producao-de-veiculos-tem-alta-de-193-em-setembro-informa-anfavea?utm_source=thenewscc&utm_medium=email&utm_campaign=referral]                 Investir é barato? Era. Agora, é de graça

PATROCINADO POR ÍON ITAÚ

Você não precisa pagar para investir com o íon. A plataforma inovou mais uma vez e acabou de zerar a taxa de corretagem.  Baixe o app e descubra seu novo jeito de investir em Ações, BDRs, ETFS e FIIs — tudo isso com Taxa Zero de corretagem.  [https://ion.itau/?utm_source=newsletter&utm_medium=e-mail&utm_campaign=11_10&utm_id=thenewscc]

Já imaginou ganhar um kit desses?PROGRAMA DE INDICAÇÃO

Isso é simplesmente fantástico. Dez leitores do nosso jornal serão presenteados com um super kit composto por um Kindle 11ª geração e uma Alexa Echo Dot 3ª geração.

Já parou pra pensar que esse leitor pode ser você? Fala sério, são 10 chances de ganhar.

E pra concorrer a esse prêmio, você só precisa indicar o the news para um amigo até sexta-feira (14/10). Simples assim.

Bônus: Dobre suas chances de ganhar a cada indicação realizada. 1 amigo = 1 chance. 4 amigos = 4 chances.

Seu kit pode estar chegando aí… Clique no botão abaixo, pegue seu link exclusivo de indicação e mande para a galera. Boa sorte!

CLIQUE PARA COMPARTILHAR [https://grow.surf/x5eg0s?utm_source=newsletter&utm_medium=orgânico&utm_campaign=sessao-copy-pi]

PS:  Clique aqui [https://thenews.substack.com/p/6b36d5e2-4c17-414b-ab38-86094fa17dbe] para conferir as regras oficiais do sorteio, que será realizado dia 17/10.

the news 📬

Mais inteligente em 5 minutos. Somos um jornal gratuito e diário, que tem por objetivo te trazer tudo que você precisa saber para começar o seu dia bem e informado.

Notícias, de fato, relevantes sobre as principais atualidades do mundo, do Brasil, tecnologia e do mercado financeiro, sempre nessa ordem.

Direto na sua caixa de entrada do e-mail favorito, sempre às 06:06. É gratuito, mas pode viciar.

🎟️  O próximo anunciante pode ser você.  É só clicar aqui [https://thenewscc.typeform.com/to/twCcjR bQ].

👍👎 Gostou da edição de hoje?  Nos conte aqui [https://docs.google.com/forms/d/12jhUljBzSvd-RQKLmpXAo7tw94QchngJEi26PTrZkxg/edit].

📱 Quer ser um influenciador do seu jornal favorito?  Clique aqui para saber mais [https://forms.gle/hHBPMFkpG2NDXWDK7].

já conhece nossas outras newsletters?

🦄  the bizness [https://thenewscc.com.br/bizness-cadastro/?utm_source=newsletter&utm_medium=orgânico&utm_campaign=sessa-recomendacao]: sua dose de conteúdo sobre os assuntos mais relevantes do mundo dos negócios. análises, números e insights.  um MBA em forma de e-mail. [https://thenewscc.com.br/bizness-cadastro/?utm_source=newsletter&utm_medium=orgânico&utm_campaign=sessa-recomendacao]

🏆  the champs [https://thenewscc.com.br/champs-cadastro/?utm_source=newsletter&utm_medium=orgânico&utm_campaign=sessa-recomendacao]: todo o não óbvio sobre os esportes, na palma da sua mão.  descontraído e direto ao ponto, como deve ser [https://thenewscc.com.br/champs-cadastro/?utm_source=newsletter&utm_medium=orgânico&utm_campaign=sessa-recomendacao].

🧸  the stories [https://thenewscc.com.br/stories/?utm_source=newsletter&utm_medium=orgânico&utm_cam paign=sessa-recomendacao]: histórias que emocionam. não tão longas quanto um romance, mas suficientes pra te fazer sentir.  contamos e escrevemos amor. [https://thenewscc.com.br/stories-cadastro/?utm_source=newsletter&utm_medium=orgânico&utm_campaign=sessa-recomendacao]

até amanhã

Sempre chegamos a sua caixa de entrada por volta das 06:06. Alguns servidores de e-mail são teimosos e atrasam… Outros são piores ainda e nos jogam para o spam e/ ou promoções. Sempre que não nos encontrar na caixa de entrada, procure nessas duas.

[https://twitter.com/thenews_br]                               mais inteligente em 5 minutos.

the news.cc | newsletter

São Paulo, SP 04506-000 | Miami, FL

Política de Privacidade [https://drive.google.com/file/d/1Yi-bty-sLL5mCBwiDWKlE2JNLDclCmVe/view?usp=sharing] |  Anuncie conosco [https://thenewscc.typeform.com/to/twCcjRbQ]

Actualizar preferências https://thenews.updatemyprofile.com/t-aditrky-851105C4-jyykiytlo-td  |   Remover subscrição https://thenews.cmail19.com/t/t-u-aditrky-jyykiytlo-th/
''',
        EXPECTED: [
            "é hora de escolher.",
            "bom dia. a parte difícil do foco não é dizer 'sim' para o seu objetivo, mas conseguir falar 'não' às várias outras possibilidades que existem. escolha com carinho.",
            "MUNDO",
            "Rússia fez maior ataque aéreo na Ucrânia desde o início da guerra.",
            "Alerta em Kiev. Ontem, depois de três meses sem ataques, a capital da Ucrânia foi fortemente bombardeada pela Rússia. Até o momento, 14 civis morreram e 97 ficaram feridos.",
            "Os principais alvos foram instalações de energia, comando militar e comunicação. Outras cidades do país também foram atacadas, o que pode indicar uma nova fase da guerra.",
            "Qual o motivo do ataque? De acordo com as falas de Putin, os mísseis são uma resposta ao bombardeio na ponte entre Rússia e Crimeia no sábado. Essa ação, inclusive, foi classificada pelo presidente russo como “ato de terrorismo internacional”.",
            "Contextualizando… Por conta da forte resistência ucraniana no primeiro semestre, a Rússia suspendeu os ataques na capital e focou seus esforços no leste e sul do país — territórios que foram anexados no último mês.",
            "🇺🇸 Depois dos ataques de ontem, Joe Biden garantiu apoio contínuo dos EUA à Ucrânia. Nas palavras do presidente americano, a cooperação militar entre os dois países será prioridade.",
            "What's next? O Ministro das Relações Exteriores da Ucrânia anunciou que o país vai continuar com ações ofensivas contra novos ataques russos. A guerra muda de fase, mas a tensão continua a mesma…",
            "O que mais foi notícia ao redor do globo?",
            "'Dia Mundial contra a Pena Capital'.",
            "Papa Francisco pede fim da pena de morte.",
            "Tribunal francês: Começou o julgamento da Air France e Airbus sobre o acidente com o voo que ia do Rio a Paris em 2009.",
            "Vítimas tropicais.",
            "A tempestade Julia deixa 14 mortos na América Central e segue para o México.",
            "BRASIL",
            "Candidatos gastaram milhões em marketing na internet.",
            "O TSE divulgou que os candidatos às Eleições Gerais de 2022 já gastaram mais de. R$ 196 milhões promovendo seus conteúdos na internet.",
            "Se for feita uma comparação com 2018, a soma do investimento total gasto nas propagandas on-line chegou a R$ 99,7 milhões, ou seja, esse número quase dobrou agora.",
            "A eleição deste ano está mostrando que não tem mais como fazer uma campanha sem considerar tráfego pago nas redes. E parece que os candidatos entenderam isso.",
            "Falando só dos presidenciáveis… Entre aqueles que lideraram as intenções de voto, Simone Tebet (MDB) foi a que mais investiu em tráfego para impulsionar os seus conteúdos — ao todo foram R$ 2,7 milhões.",
            "Logo atrás está o Lula (PT), que gastou. R$ 2,5 milhões, depois Ciro do PDT, com o valor de. R$ 1,6 milhão e, em último, Bolsonaro (PL), que gastou em torno de. R$ 530 mil.",
            "Gás final. Na última semana antes do primeiro turno, a plataforma de anúncios do Google recebeu vários acordos de prestação de serviço. Foram investidos mais. R$ 700 mil em quatro horas no Google.",
            "Bottom-line: As despesas com propagandas eleitorais na TV e no rádio estão diminuindo cada vez mais. No primeiro turno, foram registrados quase R$ 400 milhões, 15% a menos do que em 2018.",
            "Outras notícias relevantes no Brasil:",
            "Ex-presidente: STF marca julgamento de ação contra Collor na Lava Jato.",
            "Atrasos na pista… Aeroporto de Congonhas tem 300 voos cancelados depois que um avião teve o pneu furado durante o pouso.",
            "Acordos.",
            "Brasil passa a vender energia excedente para Argentina e Uruguai.",
            "TECNOLOGIA",
            "As marcas estão investindo em músicas virais do TikTok.",
            "Marketing de ouvido. Recentemente, algumas empresas começaram a desenvolver sons originais do TikTok, na esperança de bombarem e se tornarem virais no aplicativo chinês.",
            "Para as marcas, um som 'chiclete' oferece visibilidade e uma probabilidade maior de alcançar as páginas “For you” de mais usuários.",
            "Explicando… Quando um criador carrega um vídeo no TikTok com som original, outros usuários podem usar o mesmo som para criar vídeos próprios. À medida que mais pessoas usam o som original, ele vai se tornando viral.",
            "Como o algoritmo “empurra” o que está funcionando, esses sons acabam impulsionando conteúdos. Só pra ter ideia, “As It Was” de Harry Styles e “Vibe” de Cookiee Kawaii, foram usados em quase 4 milhões de vídeos.",
            "O que está acontecendo agora?",
            "As marcas estão querendo entrar no jogo, mas, por problemas de licenciamento, nem sempre têm acesso aos hits. Assim, para navegar pelas legalidades, os varejistas começaram a fazer parcerias com artistas e lançar desafios no TikTok.",
            "A Pepsi anunciou uma parceria com a cantora e atriz Chlöe Bailey, na terça-feira, para lançar uma nova versão da música “Footloose”;",
            "A American Eagle e a cantora do TikTok, Katherine Li, se uniram para criar uma versão personalizada de sua música “Happening Again”;",
            "A Pizza Hut colaborou com Jon Moss, um TikToker com quase 7 milhões de seguidores, para criar um hino que celebrasse o retorno da Detroit-Style Pizza.",
            "Zoom Out: Os varejistas vêm criando jingles na televisão e no rádio há décadas, porém, agora, o desafio é diferente. Além de se ajustarem ao vídeo curto e na vertical, as marcas estão tentando usar o algoritmo — imprevisível — ao seu favor.",
            "NEGÓCIOS",
            "Amazon vai gastar 1 bilhão de euros com veículos elétricos.",
            "Rumo ao carbono líquido zero. A Amazon anunciou, ontem, que gastará 1 bilhão de euros para eletrificar sua frota na Europa. O dinheiro será usado para dobrar o número de veículos elétricos no continente.",
            "Segundo a empresa, o investimento acelerará a inovação no setor de transporte como um todo e contribuirá para o desenvolvimento da infraestrutura de recarga de veículos.",
            "Contexto: O anúncio ocorre depois da divulgação do relatório de sustentabilidade da empresa. Apesar dos esforços para se vender como líder em ação climática, suas emissões de dióxido de carbono cresceram 18% no último ano.",
            "Nas palavras do CEO da Amazon, “a rede de transporte é uma das áreas mais desafiadoras do negócio para descarbonizar, e para alcançar o carbono líquido zero será necessário um investimento substancial e sustentável”.",
            "O mercado está de olho… 👀",
            "Embora muitas empresas de logística, incluindo gigantes como UPS e FedEx, tenham prometido comprar mais veículos elétricos de emissão zero, ainda não há muitas vans e caminhões à venda.",
            "Percebendo o movimento, várias startups estão correndo para suprir essa demanda do mercado. Da mesma forma, fabricantes maiores — General Motors, Volkswagen, Ford e Tesla — também passaram a focar nos veículos elétricos para entregas.",
            "ECONOMIA",
            "Real foi a 8ª moeda que mais se valorizou em 2022.",
            "Segundo levantamento, o real foi a 8ª moeda que mais valorizou em relação ao dólar americano em 2022. Desde o início do ano, a nossa moeda subiu 6,9%.",
            "Entre as principais economias mundiais, a moeda brasileira só valorizou menos do que a da Rússia, que já subiu 18,7% no mesmo período.",
            "📈 Ainda nos destaques positivos, o kwanza da Angola foi a moeda que teve maior alta, subindo 29,7%. Logo em seguida, ficaram o rublo russo e o dram da Armênia.",
            "📉 Na América do Sul, o pior desempenho foi da Venezuela, que viu sua moeda se desvalorizar 44%. Mas o pior desempenho do ano foi o da rúpia do Sri Lanka, fechando em 45%.",
            "O levantamento se baseou em 118 países e na zona do euro, que desvalorizou quase 14% neste ano. Se quiser ver o relatório na íntegra, é só clicar aqui.",
            "Destaques do dia:",
            "Fechamento: Ibovespa cai 0,37%, acompanhando pares internacionais em sessão de cautela; dólar cai 0,42% As contas estão apertando… Endividamento atinge 80% das famílias mais pobres em setembro.",
            "Recuperação da indústria.",
            "Produção de veículos tem alta de 19,3% em setembro."
        ]
    }
]


@Test()
def getCompleteEmailBodyList_whatMore():
    #arrange
    arranged = '''What's next? O Ministro das Relações Exteriores da Ucrânia anunciou que o país vai continuar com  ações ofensivas contra novos ataques russos [https://www.cnnbrasil.com.br/live-update/internacional/as-ultimas-noticias-da-guerra-na-ucrania-2/1978503/?utm_source=thenewscc&utm_medium=email&utm_campaign=referral]. A guerra muda de fase, mas a tensão continua a mesma...

    O que mais foi notícia ao redor do globo?

    "Dia Mundial contra a Pena Capital".  Papa Francisco pede fim da pena de morte [https://g1.globo.com/mundo/noticia/2022/10/10/papa-francisco-pede-fim-da-pena-de-morte.ghtml?utm_source=thenewscc&utm_medium=email&utm_campaign=referral]Tribunal francês:  Começou o julgamento da Air France e Airbus sobre o acidente com o voo que ia do Rio a Paris em 2009 [https://g1.globo.com/mundo/noticia/2022/10/10/comeca-julgamento-da-air-france-e-airbus-sobre-o-acidente-com-voo-af447-que-ia-de-rio-a-paris-em-2009.ghtml?utm_source=thenewscc&utm_medium=email&utm_campaign=referral]Vítimas tropicais.  A tempestade Julia deixa 14 mortos na América Central e segue para o México [https://g1.globo.com/mundo/noticia/2022/10/10/tempestade-julia-deixa-14-mortos-na-america-central-e-segue-para-o-mexico.ghtml?utm_source=thenewscc&utm_medium=email&utm_campaign=referral]                 Candidatos gastaram milhões em marketing na internet

    BRASIL

    (Ilustração | the news)

    O TSE divulgou que os candidatos às Eleições Gerais de 2022 já gastaram mais de  R$ 196 milhões [https://divulgacandcontas.tse.jus.br/divulga/?utm_source=thenewscc&utm_medium=email&utm_campaign=referral#/consulta/campanha/2022/2040602022/ranks] promovendo seus conteúdos na internet.

    Se for feita uma comparação com 2018, a soma do investimento total gasto nas propagandas on-line chegou a R$ 99,7 milhões, ou seja, esse número quase dobrou agora.'''
    expected = [
        "What's next? O Ministro das Relações Exteriores da Ucrânia anunciou que o país vai continuar com ações ofensivas contra novos ataques russos. A guerra muda de fase, mas a tensão continua a mesma…",
        "O que mais foi notícia ao redor do globo?",
        "'Dia Mundial contra a Pena Capital'.",
        "Papa Francisco pede fim da pena de morte.",
        "Tribunal francês: Começou o julgamento da Air France e Airbus sobre o acidente com o voo que ia do Rio a Paris em 2009.",
        "Vítimas tropicais.",
        "A tempestade Julia deixa 14 mortos na América Central e segue para o México.",
        "BRASIL",
        "Candidatos gastaram milhões em marketing na internet.",
        "O TSE divulgou que os candidatos às Eleições Gerais de 2022 já gastaram mais de. R$ 196 milhões promovendo seus conteúdos na internet.",
        "Se for feita uma comparação com 2018, a soma do investimento total gasto nas propagandas on-line chegou a R$ 99,7 milhões, ou seja, esse número quase dobrou agora.",
    ]

    #act
    toAssert = EmailStaticHelper.getCompiledEmailBodyList(arranged)

    #assert
    for e, t in zip(expected, toAssert):
        assert e == t, f'{e} == {t}'
    assert len(expected) == len(toAssert)
    assert ObjectHelper.equals(expected, toAssert), f'{StringHelper.prettyJson(expected)}{c.NEW_LINE}{StringHelper.prettyJson(toAssert)}'


@Test()
def getCompiledEmailBodyList_whenSentenceIsTooLargeBySemiColon():
    #arrange
    arranged = 'A Pepsi anunciou uma parceria com a cantora e atriz Chlöe Bailey, na terça-feira, para lançar uma nova versão da música “Footloose”; A American Eagle e a cantora do TikTok, Katherine Li, se uniram para criar uma versão personalizada de sua música “Happening Again”; A Pizza Hut colaborou com Jon Moss, um TikToker com quase 7 milhões de seguidores, para criar um hino que celebrasse o retorno da Detroit-Style Pizza'
    expected = [
        'A Pepsi anunciou uma parceria com a cantora e atriz Chlöe Bailey, na terça-feira, para lançar uma nova versão da música “Footloose”;',
        'A American Eagle e a cantora do TikTok, Katherine Li, se uniram para criar uma versão personalizada de sua música “Happening Again”;',
        'A Pizza Hut colaborou com Jon Moss, um TikToker com quase 7 milhões de seguidores, para criar um hino que celebrasse o retorno da Detroit-Style Pizza.'
    ]

    #act
    toAssert = EmailStaticHelper.getCompiledEmailBodyList(arranged)

    #assert
    for e, t in zip(expected, toAssert):
        assert e == t, f'{e} == {t}'
    assert len(expected) == len(toAssert)
    assert ObjectHelper.equals(expected, toAssert), f'{StringHelper.prettyJson(expected)}{c.NEW_LINE}{StringHelper.prettyJson(toAssert)}'


@Test()
def getCompiledEmailBodyList_badSequence():
    arranged = """Numericamente falando:

    Estima-se que a medida iria gerar um aumento dos gastos de mais de R$ 4 bilhões para municípios e de até R$ 1,3 bi para estados.

    Na prática, isso poderia implicar a demissão de mais de 80 mil profissionais e o fechamento de 20 mil leitos em decorrência dessa "simples" mudança do piso salarial.

    Após analisar melhor o caso, o  Ministro do STF atendeu os pedidos de entidades do setor médico  [https://www.poder360.com.br/justica/barroso-suspende-aplicacao-do-piso-salarial-da-enfermagem/?utm_source=Feed+UOL&utm_medium=onebox&utm_campaign=news/09/04/ministro-barroso-do-stf-suspende-piso-da-enfermagem.ghtml?utm_source=Feed+UOL&utm_medium=onebox&utm_campaign=news]que indicaram risco e decidiu que, para que a Lei possa valer, estados,  municípios e alguns outros interessados devem se posicionar sobre o impacto real da mudança. [https://www.poder360.com.br/justica/barroso-suspende-aplicacao-do-piso-salarial-da-enfermagem/?utm_source=Feed+UOL&utm_medium=onebox&utm_campaign=news/09/04/ministro-barroso-do-stf-suspende-piso-da-enfermagem.ghtml?utm_source=Feed+UOL&utm_medium=onebox&utm_campaign=news]

    Mais notícias no cenário nacional…

    O lado B do Rock in Rio.  Nos dois primeiros dias de shows, a Companhia de Limpeza Urbana já recolheu 110 toneladas de lixo [https://agenciabrasil.ebc.com.br/geral/noticia/2022-09/em-dois-dias-comlurb-recolhe-110-toneladas-de-residuos-no-rock-rio?utm_source=Feed+UOL&utm_medium=onebox&utm_campaign=news]Ele é pop mesmo…  Agronegócio emprega mais de 19 milhões de pessoas em 2022 [https://www.cnnbrasil.com.br/business/conexao-agro-agronegocio-brasileiro-emprega-mais-de-19-milhoes-em-2022/?utm_source=Feed+UOL&utm_medium=onebox&utm_campaign=news]Sobrou pra ela...  Polícia argentina prende namorada de brasileiro acusado de atacar Cristina Kirchner [https://oglobo.globo.com/mundo/noticia/2022/09/policia-argentina-prende-namorada-de-brasileiro-acusado-de-atacar-cristina-kirchner.ghtml?utm_source=globo.com&utm_medium=oglobo]                         OnlyFans já gerou quase US$ 4 bilhões aos influenciadores

    OnlyFans já gerou quase US$ 4 bilhões aos influenciadoresTECNOLOGIA

    (Imagem: Tube Filter | Reprodução)

    Muita gente gosta do clima quente. O OnlyFans, serviço de conteúdos sexuais por assinatura, anunciou seus resultados financeiros no ano passado — e eles foram pra lá de animadores.

    A receita líquida da empresa cresceu 160%, chegando a  US$ 932 milhões [https://variety.com/2022/digital/news/onlyfans-financials-earnings-creators-1235357264/?utm_source=thenewscc&utm_medium=email&utm_campaign=referral], com direito ao seu maior crescimento anual nos lucros, atingindo US$ 433 milhões. Resumindo: muito dinheiro. risos.

    💰 Bem interessante. Os criadores de conteúdo do OnlyFans ganharam  US$ 3,9 bilhões em 2021 [https://variety.com/2022/digital/news/onlyfans-financials-earnings-creators-1235357264/?utm_source=thenewscc&utm_medium=email&utm_campaign=referral], um aumento de 115% em relação a 2020. A quantia depositada na conta dos criadores da plataforma sensual já se aproxima de 10 bilhões de dólares desde sua fundação, em 2016."""
    expected = [
        "Numericamente falando:",
        "Estima-se que a medida iria gerar um aumento dos gastos de mais de R$ 4 bilhões para municípios e de até R$ 1,3 bi para estados.",
        "Na prática, isso poderia implicar a demissão de mais de 80 mil profissionais e o fechamento de 20 mil leitos em decorrência dessa 'simples' mudança do piso salarial.",
        "Após analisar melhor o caso, o Ministro do STF atendeu os pedidos de entidades do setor médico que indicaram risco e decidiu que:",
        "para que a Lei possa valer, estados, municípios e alguns outros interessados devem se posicionar sobre o impacto real da mudança.",
        "Mais notícias no cenário nacional…",
        "O lado B do Rock in Rio.",
        "Nos dois primeiros dias de shows, a Companhia de Limpeza Urbana já recolheu 110 toneladas de lixo.",
        "Ele é pop mesmo… Agronegócio emprega mais de 19 milhões de pessoas em 2022.",
        "Sobrou pra ela… Polícia argentina prende namorada de brasileiro acusado de atacar Cristina Kirchner.",
        "OnlyFans já gerou quase US$ 4 bilhões aos influenciadores.",
        "TECNOLOGIA",
        "OnlyFans já gerou quase US$ 4 bilhões aos influenciadores.",
        "Muita gente gosta do clima quente. O OnlyFans, serviço de conteúdos sexuais por assinatura, anunciou seus resultados financeiros no ano passado — e eles foram pra lá de animadores.",
        "A receita líquida da empresa cresceu 160%, chegando a US$ 932 milhões, com direito ao seu maior crescimento anual nos lucros, atingindo US$ 433 milhões. Resumindo: muito dinheiro. risos.",
        "💰 Bem interessante.",
        "Os criadores de conteúdo do OnlyFans ganharam.",
        "US$ 3,9 bilhões em 2021, um aumento de 115% em relação a 2020.",
        "A quantia depositada na conta dos criadores da plataforma sensual já se aproxima de 10 bilhões de dólares desde sua fundação, em 2016."
    ]

    #act
    toAssert = EmailStaticHelper.getCompiledEmailBodyList(arranged)

    #assert
    for e, t in zip(expected, toAssert):
        assert e == t, f'{e} == {t}'
    assert ObjectHelper.equals(expected, toAssert), f'{StringHelper.prettyJson(expected)}{c.NEW_LINE}{StringHelper.prettyJson(toAssert)}'
    assert len(expected) == len(toAssert)


@Test()
def getCompiledEmailBodyList_comaSplitNonsense():
    arranged = """Após analisar melhor o caso, o  Ministro do STF atendeu os pedidos de entidades do setor médico  [https://www.poder360.com.br/justica/barroso-suspende-aplicacao-do-piso-salarial-da-enfermagem/?utm_source=Feed+UOL&utm_medium=onebox&utm_campaign=news/09/04/ministro-barroso-do-stf-suspende-piso-da-enfermagem.ghtml?utm_source=Feed+UOL&utm_medium=onebox&utm_campaign=news]que indicaram risco e decidiu que, para que a Lei possa valer, estados,  municípios e alguns outros interessados devem se posicionar sobre o impacto real da mudança. [https://www.poder360.com.br/justica/barroso-suspende-aplicacao-do-piso-salarial-da-enfermagem/?utm_source=Feed+UOL&utm_medium=onebox&utm_campaign=news/09/04/ministro-barroso-do-stf-suspende-piso-da-enfermagem.ghtml?utm_source=Feed+UOL&utm_medium=onebox&utm_campaign=news]"""
    expected = [
        "Após analisar melhor o caso, o Ministro do STF atendeu os pedidos de entidades do setor médico que indicaram risco e decidiu que:",
        "para que a Lei possa valer, estados, municípios e alguns outros interessados devem se posicionar sobre o impacto real da mudança."
    ]

    #act
    toAssert = EmailStaticHelper.getCompiledEmailBodyList(arranged)

    #assert
    for e, t in zip(expected, toAssert):
        assert e == t, f'{e} == {t}'
    assert ObjectHelper.equals(expected, toAssert), f'{StringHelper.prettyJson(expected)}{c.NEW_LINE}{StringHelper.prettyJson(toAssert)}'
    assert len(expected) == len(toAssert)


@Test()
def getCompiledEmailBodyList_specificCase_tooManyeSpaces():
    #arrange
    arranged = """O impacto nas companhias

    O combustível representa 50% dos custos da Azul e Gol, por exemplo. No entanto, a redução de preço, não chega a ser um alívio sobre os gastos.

    Zoom in: Entre julho de 2019, e o mesmo período de 2022, o combustível de aviação  subiu quase 170%. [https://www.infomoney.com.br/mercados/goll4-azul4-combustivel-da-aviacao-fica-mais-barato-a-partir-de-hoje-mas-nao-consegue-aliviar-custos-das-aereas/?utm_source=thenewscc&utm_medium=email&utm_campaign=referral]Nesse intervalo, o valor do diesel e da gasolina avançaram ao entorno de  125%. [https://www.infomoney.com.br/mercados/goll4-azul4-combustivel-da-aviacao-fica-mais-barato-a-partir-de-hoje-mas-nao-consegue-aliviar-custos-das-aereas/?utm_source=thenewscc&utm_medium=email&utm_campaign=referral]

    Essa forte volatilidade, aliada à negociação do valor de aluguel das aeronaves da época da pandemia, dificulta a projeção de redução nos preços.

    O que acontecerá nesta semana? 📅

    CALENDÁRIO DA SEMANA

    🏢 Labor Day: Hoje, as bolsas dos EUA estão fechadas em função do Dia do Trabalho.

    🇪🇺 Reunião do Banco Central Europeu: Na agenda internacional, a semana está cheia. O momento mais   aguardado é a reunião do BCE,  que decidirá sobre a taxa de juros do bloco europeu [https://www.infomoney.com.br/mercados/ipca-de-agosto-reuniao-do-banco-central-e-europeu-e-conversa-com-jerome-powell-o-que-acompanhar-na-semana/?utm_source=thenewscc&utm_medium=email&utm_campaign=referral]. A previsão é de uma alta de 0,75 ponto percentual.

    🇧🇷 Dia da Independência: Por aqui, na quarta-feira,  teremos um feriado que promete ser movimentad  o [https://www.infomoney.com.br/mercados/ipca-de-agosto-reuniao-do-banco-central-e-europeu-e-conversa-com-jerome-powell-o-que-acompanhar-na-semana/?utm_source=thenewscc&utm_medium=email&utm_campaign=referral]. Nosso 7 de Setembro será marcado por manifestações políticas, esperadas e planejadas já há algum tempo.

    🇺🇸 Jerome Powell: O presidente do Federal Reserve participará, nesta semana, de um evento que será   transmitido ao vivo e promete atrair muita atenção.  Será a primeira fala de Powell depois de Jackson Hole [https://www.infomoney.com.br/mercados/ipca-de-agosto-reuniao-do-banco-central-e-europeu-e-conversa-com-jerome-powell-o-que-acompanhar-na-semana/?utm_source=thenewscc&utm_medium=email&utm_campaign=referral]. Stay tunned.

    📊 IPCA: Na sexta-feira, será divulgado o Índice de Preços ao Consumidor Amplo referente a agosto,  um importante indicador da inflação [https://www.infomoney.com.br/mercados/ipca-de-agosto-reuniao-do-banco-central-e-europeu-e-conversa-com-jerome-powell-o-que-acompanhar-na-semana/?utm_source=thenewscc&utm_medium=email&utm_campaign=referral]. A média da projeção dos economistas é de uma deflação — a segunda seguida — de 0,39%.

    SegundinhaPROGRAMA DE INDICAÇÃO

    Toda segunda feira traz uma nova chance. Use o dia de hoje para guiar o resto da semana, e fazer dela a melhor de todas.

    Pensando nisso, que tal utilizar uma parte do seu tempo para conquistar prêmios?"""
    expected = [
        "O impacto nas companhias.",
        "O combustível representa 50% dos custos da Azul e Gol, por exemplo. No entanto, a redução de preço, não chega a ser um alívio sobre os gastos.",
        "Zoom in: Entre julho de 2019, e o mesmo período de 2022, o combustível de aviação subiu quase 170%. Nesse intervalo, o valor do diesel e da gasolina avançaram ao entorno de 125%.",
        "Essa forte volatilidade, aliada à negociação do valor de aluguel das aeronaves da época da pandemia, dificulta a projeção de redução nos preços.",
        "CALENDÁRIO DA SEMANA",
        "O que acontecerá nesta semana? 📅",
        "🏢 Labor Day: Hoje, as bolsas dos EUA estão fechadas em função do Dia do Trabalho.",
        "🇪🇺 Reunião do Banco Central Europeu: Na agenda internacional, a semana está cheia. O momento mais aguardado é a reunião do BCE, que decidirá sobre a taxa de juros do bloco europeu. A previsão é de uma alta de 0,75 ponto percentual.",
        "🇧🇷 Dia da Independência: Por aqui, na quarta-feira, teremos um feriado que promete ser movimentad o. Nosso 7 de Setembro será marcado por manifestações políticas, esperadas e planejadas já há algum tempo.",
        "🇺🇸 Jerome Powell: O presidente do Federal Reserve participará, nesta semana, de um evento que será transmitido ao vivo e promete atrair muita atenção. Será a primeira fala de Powell depois de Jackson Hole. Stay tunned.",
        "📊 IPCA: Na sexta-feira, será divulgado o Índice de Preços ao Consumidor Amplo referente a agosto, um importante indicador da inflação. A média da projeção dos economistas é de uma deflação — a segunda seguida — de 0,39%."
    ]

    #act
    toAssert = EmailStaticHelper.getCompiledEmailBodyList(arranged)

    #assert
    for e, t in zip(expected, toAssert):
        assert e == t, f'{e} == {t}'
    assert ObjectHelper.equals(expected, toAssert), f'{StringHelper.prettyJson(expected)}{c.NEW_LINE}{StringHelper.prettyJson(toAssert)}'
    assert len(expected) == len(toAssert)


@Test()
def getCompiledEmailBodyList_whenWhatMore():
    #arrange
    arranged = """A relevância 🇧🇷

    Os brasileiros estão na liderança como a maior comunidade imigrante em território português, representando  29% dos estrangeiros em situação regular no país [https://www1.folha.uol.com.br/mundo/2022/06/portugal-encaminha-pacotao-de-vistos-e-cria-permissao-especial-a-quem-procura-trabalho.shtml?utm_source=thenewscc&utm_medium=email&utm_campaign=referral].

    No entanto, como muitos imigrantes chegam como turistas e começam a trabalhar ilegalmente, os números reais são maiores. Aos simplificar a autorização, será mais fácil controlar as condições dos trabalhadores estrangeiros.

    O que mais é destaque mundialmente falando?

    Clima tenso em Quito.  Manifestantes bloqueiam acesso à capital do Equador [https://g1.globo.com/mundo/noticia/2022/06/16/manifestantes-bloqueiam-acesso-a-capital-do-equador-apesar-de-apelo-ao-dialogo-por-parte-do-governo.ghtml?utm_source=thenewscc&utm_medium=email&utm_campaign=referral]

    Conflito geopolítico.  Líderes europeus fazem visita inédita à Ucrânia [https://g1.globo.com/mundo/noticia/2022/06/16/lideres-europeus-fazem-visita-inedita-a-ucrania.ghtml?utm_source=thenewscc&utm_medium=email&utm_campaign=referral]

    Ainda na Europa...  Ações europeias atingem mínima de 16 meses após aumentos de juros [https://www.infomoney.com.br/mercados/acoes-europeias-atingem-minima-de-16-meses-apos-aumentos-de-juros/]

    Os gamers já podem comemorar 👾BRASIL

    (Imagem: Philippe Wojazer | Reprodução)

    Redução de tributos. Enquanto muitos jogadores aproveitaram o feriado para passar de nível nos seus games preferidos, o presidente Jair Bolsonaro editou, ontem, um novo decreto que  reduziu os impostos sobre jogos eletrônicos [https://agenciabrasil.ebc.com.br/geral/noticia/2022-06/presidente-anuncia-nova-reducao-de-impostos-para-jogos-eletronicos?utm_source=thenewscc&utm_medium=email&utm_campaign=referral].

    Na prática… A partir de julho, a alíquota de importação de partes e acessórios dos consoles e das máquinas de videogame cairá de 16% para 12%."""
    expected = [
        "A relevância 🇧🇷",
        "Os brasileiros estão na liderança como a maior comunidade imigrante em território português, representando 29% dos estrangeiros em situação regular no país.",
        "No entanto, como muitos imigrantes chegam como turistas e começam a trabalhar ilegalmente, os números reais são maiores. Aos simplificar a autorização, será mais fácil controlar as condições dos trabalhadores estrangeiros.",
        "O que mais é destaque mundialmente falando?",
        "Clima tenso em Quito. Manifestantes bloqueiam acesso à capital do Equador.",
        "Conflito geopolítico. Líderes europeus fazem visita inédita à Ucrânia.",
        "Ainda na Europa… Ações europeias atingem mínima de 16 meses após aumentos de juros.",
        "BRASIL",
        "Os gamers já podem comemorar 👾",
        "Redução de tributos. Enquanto muitos jogadores aproveitaram o feriado para passar de nível nos seus games preferidos, o presidente Jair Bolsonaro editou, ontem, um novo decreto que reduziu os impostos sobre jogos eletrônicos.",
        "Na prática… A partir de julho, a alíquota de importação de partes e acessórios dos consoles e das máquinas de videogame cairá de 16% para 12%."
    ]

    #act
    toAssert = EmailStaticHelper.getCompiledEmailBodyList(arranged)

    #assert
    for e, t in zip(expected, toAssert):
        assert e == t, f'{e} == {t}'
    assert ObjectHelper.equals(expected, toAssert), f'{StringHelper.prettyJson(expected)}{c.NEW_LINE}{StringHelper.prettyJson(toAssert)}'
    assert len(expected) == len(toAssert)


@Test()
def getCompiledEmailBodyList_whenTooManyLinks():
    #arrange
    arranged = """O medo é claro. Uma desaceleração no crescimento,  depois de uma avaliação de US$ 13,3 bilhões [https://techcrunch.com/2022/07/14/nft-marketplace-opensea-lays-off-20-percent-of-its-staff-we-have-entered-crypto-winter/?utm_source=thenewscc&utm_medium=email&utm_campaign=referral] com a corrida de alta da criptomoeda de 2021.

    (Imagem: Pinterest | Reprodução)

    Falando em tokens e mudando de estação… No mesmo dia das demissões da OpenSea,  o Itaú anunciou que está aderindo [https://www.infomoney.com.br/mercados/itau-lanca-plataforma-de-tokenizacao-de-ativos/?utm_source=thenewscc&utm_medium=email&utm_campaign=referral]   [https://www.infomoney.com.br/mercados/itau-lanca-plataforma-de-tokenizacao-de-ativos/?utm_source=thenewscc&utm_medium=email&utm_campaign=referral] à tokenização [https://www.infomoney.com.br/mercados/itau-lanca-plataforma-de-tokenizacao-de-ativos/?utm_source=thenewscc&utm_medium=email&utm_campaign=referral] e vai emitir, distribuir e negociar ativos financeiros digitalizados — basicamente, ativos tradicionais que viram representações digitais.

    A nova unidade se chamará Itaú Digital Assets, marcando uma  entrada considerada inevitável pela companhia [https://www.infomoney.com.br/mercados/itau-lanca-plataforma-de-tokenizacao-de-ativos/?utm_source=thenewscc&utm_medium=email&utm_campaign=referral] no mundo de criptoativos. Ninguém vai ficar de fora."""
    expected = [
        "O medo é claro. Uma desaceleração no crescimento, depois de uma avaliação de US$ 13,3 bilhões com a corrida de alta da criptomoeda de 2021.",
        "Falando em tokens e mudando de estação…",
        "No mesmo dia das demissões da OpenSea, o Itaú anunciou que está aderindo à tokenização e vai emitir, distribuir e negociar ativos financeiros digitalizados — basicamente, ativos tradicionais que viram representações digitais.",
        "A nova unidade se chamará Itaú Digital Assets, marcando uma entrada considerada inevitável pela companhia no mundo de criptoativos. Ninguém vai ficar de fora."
    ]

    #act
    toAssert = EmailStaticHelper.getCompiledEmailBodyList(arranged)

    #assert
    for e, t in zip(expected, toAssert):
        assert e == t, f'{e} == {t}'
    assert ObjectHelper.equals(expected, toAssert), f'{StringHelper.prettyJson(expected)}{c.NEW_LINE}{StringHelper.prettyJson(toAssert)}'
    assert len(expected) == len(toAssert)


@Test()
def getCompiledEmailBodyList_whenTooClutered():
    #arrange
    arranged = """O lado B do Rock in Rio.  Nos dois primeiros dias de shows, a Companhia de Limpeza Urbana já recolheu 110 toneladas de lixo [https://agenciabrasil.ebc.com.br/geral/noticia/2022-09/em-dois-dias-comlurb-recolhe-110-toneladas-de-residuos-no-rock-rio?utm_source=Feed+UOL&utm_medium=onebox&utm_campaign=news]Ele é pop mesmo…  Agronegócio emprega mais de 19 milhões de pessoas em 2022 [https://www.cnnbrasil.com.br/business/conexao-agro-agronegocio-brasileiro-emprega-mais-de-19-milhoes-em-2022/?utm_source=Feed+UOL&utm_medium=onebox&utm_campaign=news]Sobrou pra ela...  Polícia argentina prende namorada de brasileiro acusado de atacar Cristina Kirchner [https://oglobo.globo.com/mundo/noticia/2022/09/policia-argentina-prende-namorada-de-brasileiro-acusado-de-atacar-cristina-kirchner.ghtml?utm_source=globo.com&utm_medium=oglobo]"""
    expected = [
        "O lado B do Rock in Rio.",
        "Nos dois primeiros dias de shows, a Companhia de Limpeza Urbana já recolheu 110 toneladas de lixo.",
        "Ele é pop mesmo… Agronegócio emprega mais de 19 milhões de pessoas em 2022.",
        "Sobrou pra ela… Polícia argentina prende namorada de brasileiro acusado de atacar Cristina Kirchner."
    ]

    #act
    toAssert = EmailStaticHelper.getCompiledEmailBodyList(arranged)

    #assert
    for e, t in zip(expected, toAssert):
        assert e == t, f'{e} == {t}'
    assert len(expected) == len(toAssert)
    assert ObjectHelper.equals(expected, toAssert), f'{StringHelper.prettyJson(expected)}{c.NEW_LINE}{StringHelper.prettyJson(toAssert)}'


@Test()
def getCompiledEmailBodyList():
    for test in EMAILS_ARRANGED_AND_EXPECTED_LIST:
        #arrange
        arranged = test.get(ARRANGED)
        expected = test.get(EXPECTED)

        #act
        toAssert = EmailStaticHelper.getCompiledEmailBodyList(arranged)

        #assert
        for e, t in zip(expected, toAssert):
            assert e == t, f'{e} == {t}'
        assert ObjectHelper.equals(expected, toAssert), f'{StringHelper.prettyJson(expected)}{c.NEW_LINE}{StringHelper.prettyJson(toAssert)}'
        assert len(expected) == len(toAssert)


@Test()
def cutAndAppendCuttedSentences():
    #arrange
    strippedSentence = '🥼 Está causando polêmica…2 O Conselho Nacional de Saúde, um braço do Ministério da Saúde, aprovou um documento que defende o reconhecimento de terreiros e casas religiosas de Matriz Africana como promotores de saúde e cura complementares do SUS, além da legalização do aborto e da maconha'
    preCompiledEmailBodyList = []
    noneExceptionExpected = None
    expected = [
        '🥼 Está causando polêmica…',
        '2 O Conselho Nacional de Saúde, um braço do Ministério da Saúde, aprovou um documento que defende o reconhecimento de terreiros e casas religiosas de Matriz Africana como promotores de saúde e cura complementares do SUS,',
        'além da legalização do aborto e da maconha'
    ]

    #act
    #assert
    try:
        EmailStaticHelper.cutAndAppendCuttedSentences(
            strippedSentence, 
            NewsConstant.CUT_SENTENCE_CUT_LIST, 
            preCompiledEmailBodyList
        )
    except Exception as raisedException:
        noneExceptionExpected = raisedException

    
    assert ObjectHelper.isNone(noneExceptionExpected), noneExceptionExpected
    assert ObjectHelper.equals(expected, preCompiledEmailBodyList), f'''{StringHelper.prettyPython(expected)} == {StringHelper.prettyPython(preCompiledEmailBodyList)}'''


NEW_BODY = '''Ver imagem: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/2d969d51-2444-4da2-968a-b8b1a67c50b7/ALURA.png)
Seguir link da imagem: (https://www.alura.com.br/imersao-dados-ia?utm_source=thenews&utm_medium=cpc&utm_campaign=imersao-dados_ia&utm_id=tn_1&utm_content=middle2108)
Caption:

## **bem e informado**

##### bom dia. seja bem-vindo ao jornal que te deixa não só bem-informado, mas bem e informado. há uma singela diferença. que seja mais uma belíssima semana.

Ver imagem: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/b8b1d4ec-53c6-4348-b78a-ec8df3b25302/MAIS_INTELIGENTE_EM_5_MINUTOS.png)
Caption:

## **Ozempic e Wegovy estão inclinando a balança econômica da Dinamarca**

###### MUNDO

Ver imagem: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/f66a85a9-ed77-4b52-bc71-cd1290512e96/image__27_.jpeg)
Caption: (Imagem: Getty Images | Reprodução)

A Dinamarca está vendo a sua economia ser afetada positivamente pela Novo Nordisk, responsável pelos “remédios do momento”, que são [usados para diabetes e perda de peso](https://www.wsj.com/economy/central-banking/americas-obsession-with-weight-loss-drugs-is-affecting-the-economy-of-denmark-22797e5c?utm_source=thenewscc&utm_medium=email&utm_campaign=referral).

O valor de mercado da fabricante do Ozempic e do Wegovy acaba de chegar em [US$ 419 bilhões](https://www.wsj.com/economy/central-banking/americas-obsession-with-weight-loss-drugs-is-affecting-the-economy-of-denmark-22797e5c?utm_source=thenewscc&utm_medium=email&utm_campaign=referral), **ultrapassando nada menos que o PIB da Dinamarca**, o país de origem da empresa.

Graças às vendas massivas dos medicamentos ao redor do mundo, a moeda local passou por uma valorização em relação ao euro.

Isso fez com que o banco central dinamarquês baixasse as taxas de juros, indo na [contramão](https://www.infomoney.com.br/economia/bce-eleva-novamente-os-juros-em-25-pontos-base/?utm_source=the%20news&utm_medium=newsletter&utm_campaign=21_08) do movimento mais recente do Banco Central Europeu.

### “É bom, mas nem tanto…”

Para um país com apenas 5 milhões de habitantes — metade da Grande São Paulo —, ter uma empresa nacional desempenhando um papel tão desproporcional na economia pode ser arriscado.

“A **Finlândia**, que foi dominada pela Nokia e viu um [aumento de 55% no PIB entre 1995 e 2007](https://www.wsj.com/economy/central-banking/americas-obsession-with-weight-loss-drugs-is-affecting-the-economy-of-denmark-22797e5c?utm_source=thenewscc&utm_medium=email&utm_campaign=referral), teve uma década de estagnação e queda na renda per capita depois do declínio da companhia.“ —

A Novo Nordisk, agora, é a [segunda empresa pública mais valiosa da Europa](https://www.wsj.com/economy/central-banking/americas-obsession-with-weight-loss-drugs-is-affecting-the-economy-of-denmark-22797e5c?utm_source=thenewscc&utm_medium=email&utm_campaign=referral), ficando atrás apenas do conglomerado de luxo LVMH, de propriedade do Bernard Arnault — um dos homens mais ricos do mundo.

**O que mais é destaque pelo mundo?**

* **Após eleições tensas e violentas:** [Com +90% apurado, candidata de esquerda e empresário disputarão 2° turno no Equador](https://www.cnnbrasil.com.br/internacional/quem-sao-luisa-gonzalez-e-daniel-noboa-presidenciaveis-que-disputarao-2o-turno-no-equador/?utm_source=the%20news&utm_medium=newsletter&utm_campaign=21_08)

* **Xi Jinping não gostou disso:** [EUA, Japão e Coreia do Sul fazem sua primeira cúpula trilateral](https://thenewscc.com.br/mundo/eua-japao-e-coreia-do-sul-fazem-sua-primeira-cupula-trilateral/)

* **Furacão Hillary: **[Depois de passar pelo México, autoridades da Califórnia alertam para inundações com risco de vida](https://www.nbcnews.com/news/weather/live-blog/hurricane-hilary-live-updates-storm-warning-flooding-california-rcna100823?utm_source=the%20news&utm_medium=newsletter&utm_campaign=21_08)

## **STF forma maioria para que juízes possam julgar clientes de familiares**

###### **BRASIL**

Ver imagem: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/e599261b-8b6a-45de-9782-a74c4c54372f/STF.jpg)
Caption: (Imagem: O Globo | Reprodução)

**Novidade no mundo jurídico.** O Supremo Tribunal Federal formou maioria para permitir que juízes atuem em processos que envolvam [clientes de escritórios de advocacia de seus familiares](https://www.poder360.com.br/justica/stf-forma-maioria-para-que-juizes-julguem-clientes-de-familiares/).

A regra atual define que isso não pode acontecer, sob um entendimento de que pode haver algum possível conflito de interesses.** Agora, isso deve mudar.**

**Dando um exemplo real… **O antigo escritório de advocacia do novo ministro do Supremo, Cristiano Zanin, que agora é administrado somente por sua esposa, [atua em 14 diferentes processos que estão tramitando no STF](https://www.terra.com.br/noticias/brasil/politica/zanin-vota-para-permitir-que-magistrados-julguem-clientes-de-familiares,014ea665fa133b32c5f632957e4d13712t7y9slz.html?utm_source=the%20news&utm_medium=newsletter&utm_campaign=21_08).

Antes, Zanin **ficaria de fora da votação desses processos**, por envolver uma parente sua. Com o entendimento da lei mudando,** ele fica apto para julgar todos eles.**

### **As justificativas 👨🏻‍⚖️**

A ação foi apresentada pela **Associação dos Magistrados Brasileiros**, que argumentou que é “impossível” para um juiz conhecer todos os processos em que [uma empresa é representada por um escritório onde um parente trabalhe](https://saobentoemfoco.com.br/stf-forma-maioria-para-permitir-que-juizes-julguem-clientes-de-escritorios-de-advocacia-de-familiares/?utm_source=thenewscc&utm_medium=email&utm_campaign=referral).

Na outra ponta, **todas as instituições consultadas** — incluindo [Câmara, Senado e Presidência da República](https://saobentoemfoco.com.br/stf-forma-maioria-para-permitir-que-juizes-julguem-clientes-de-escritorios-de-advocacia-de-familiares/?utm_source=thenewscc&utm_medium=email&utm_campaign=referral) — se opuseram ao pedido, argumentando que o atual impedimento ajuda a manter a imparcialidade dos juízes.

“Inclusive, os **ministros que têm filhos ou cônjuges na advocacia**, como [Zanin, Gilmar, Toffoli, Moraes, Fux, Barroso e Fachin](https://jovempan.com.br/noticias/politica/stf-forma-maioria-para-permitir-que-juizes-julguem-clientes-de-escritorios-de-advocacia-de-familiares.html?utm_source=thenewscc&utm_medium=email&utm_campaign=referral), devem ser impactados diretamente com a decisão.“ —

**Falando em STF…** O Tribunal também formou maioria para manter a decisão do ministro Alexandre de Moraes que [proibiu a remoção forçada de pessoas em situação de rua](https://noticias.r7.com/brasilia/stf-forma-maioria-para-manter-proibicao-de-remocoes-forcadas-de-pessoas-em-situacao-de-rua-20082023?utm_source=thenewscc&utm_medium=email&utm_campaign=referral). **O pessoal de Brasília trabalhou muito no final de semana. risos.**

**Além disso, o que mais é destaque por aqui?**

* **"Não recebi nada”. **[Bolsaro dá entrevista exclusiva comentando o caso das joias e quebra de sigilo determinada por Moraes](https://www.youtube.com/watch?v=iVYFfUxgF0g&utm_source=the%20champs&utm_medium=newsletter&utm_campaign=21_08)

* **Boletim médico:** [Faustão, internado há 15 dias, aguarda transplante do coração](https://www.uol.com.br/splash/colunas/lucas-pasin/2023/08/20/internado-ha-15-dias-faustao-aguarda-transplante-cardiaco-diz-boletim.htm?utm_source=the%20news&utm_medium=newsletter&utm_campaign=21_08)

* **Gerou revolta: **[123Milhas cancela pacotes de passagens de sua linha promocional e diz que reembolso será em forma de voucher](https://www.cnnbrasil.com.br/economia/agencia-123-milhas-suspende-pacotes-e-emissao-de-passagens-da-linha-promocional/?utm_source=the%20news&utm_medium=newsletter&utm_campaign=21_08)

## **Cientistas recriam música do Pink Floyd lendo sinais cerebrais de ouvintes**

###### **TECNOLOGIA**

Ver imagem: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/2979ada5-0d5d-4bec-bc3b-f49711d9c545/image__16_.gif)
Caption: (GIF: Tenor | Reprodução)

**“We don’t need no education”.** Depois de treinar um computador para analisar a atividade cerebral em reação à música, foi reproduzida uma [versão abafada desse clássico do Pink Floyd](https://www.nytimes.com/2023/08/15/science/music-brain-pink-floyd.html?utm_source=thenewscc&utm_medium=email&utm_campaign=referral).

* Usando a inteligência artificial a partir das ondas cerebrais dos ouvintes, esse foi o [primeiro experimento](https://www1.folha.uol.com.br/ciencia/2023/08/pink-floyd-faz-sucesso-quando-cientistas-recriam-musica-a-partir-da-atividade-cerebral.shtml) a **reconstruir uma música através de sinais neurais.**

**Como funcionou?** Como parte de um tratamento da epilepsia — distúrbio que pode causar convulsões —, alguns pacientes tiveram uma [rede de eletrodos](https://www.nytimes.com/2023/08/15/science/music-brain-pink-floyd.html) implantados em seus cérebros.

Isso criou uma oportunidade para os neurocientistas registrarem a atividade cerebral deles enquanto ouviam música, confirmando [ideias antigas sobre os papéis de cada parte do nosso cérebro](https://www.ft.com/content/56a2aa75-390d-4d91-b607-5e132f958e8c?utm_source=thenewscc&utm_medium=email&utm_campaign=referral).

“Embora os dois lados trabalhem em conjunto, a linguagem é mais processada pelo lado esquerdo, enquanto a música é _[“mais distribuída, com viés pra direita”](https://www.ft.com/content/56a2aa75-390d-4d91-b607-5e132f958e8c?utm_source=thenewscc&amp;utm_medium=email&amp;utm_campaign=referral)_.“ —

**A relevância:** Essas descobertas oferecem um primeiro passo significativo para a criação de dispositivos que ajudem as pessoas que não conseguem falar.

Isso porque, ao entender melhor [como o cérebro processa a música](https://www.ft.com/content/56a2aa75-390d-4d91-b607-5e132f958e8c?utm_source=thenewscc&utm_medium=email&utm_campaign=referral), os cientistas não conseguem apenas reconstruir palavras isoladas, mas também o ritmo, a entonação e a emoção da fala.

🤔** Por que Pink Floyd?** A equipe escolheu a música, em parte, porque os pacientes mais velhos gostaram dela. Além disso, seus [41 segundos de letra e 2 minutos e meio de instrumentos](https://www.nytimes.com/2023/08/15/science/music-brain-pink-floyd.html?utm_source=thenewscc&utm_medium=email&utm_campaign=referral) ajudaram na diferenciação de palavras versus melodia.

## **Quanto você pagaria em uma newsletter quinzenal?**

###### **THE JOBS**

Ver imagem: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/0fde651e-5871-4029-97c9-a743e0bac46e/imagens_the_news__5_.png)
Caption:

**Pergunta errada. **Na verdade, quanto você pagaria para poder desenvolver sua carreira, ser percebido pelo seu gestor, conseguir manter seu time alinhado, ter acesso a _frameworks _para situações difíceis do dia a dia do mundo corporativo...

Quanto você pagaria para ter alguém que já tem experiência no mercado respondendo as suas perguntas de maneira personalizada sobre os dilemas do seu atual momento?

“**Não... **Não precisa arrastar pra cima e assinar uma masterclass ou uma mentoria com um desses gurus da internet.“ —

A ideia do the jobs é trazer cada um desses pontos em um** formato simples e objetivo, que seja agradável de consumir** — exatamente no estilo the news que você já conhece bem.

**Não** prometemos que seu salário vai_ aumentar em tantas vezes em apenas um mês_, ou que_ você será promovido em tempo recorde! _**Não fazemos mágica, e o "trabalho sujo" continuará sendo seu.**

Mas, fornecendo ferramentas, exercícios, conselhos práticos, dicas, insights e algumas boas histórias,** faremos de tudo para te impulsionar ao seu objetivo de se destacar na carreira.**

📠 _[Clique para ler alguns conteúdos e assine para já receber nossa edição de hoje, às 17:17](https://www.thejobscc.com.br/?utm_source=newsletter&utm_campaign=thejobs&utm_id=thenews)_.

## **Espanha é campeã da Copa Feminina e embolsa US$ 16 mi **

###### **ESPORTE**

Ver imagem: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/4e3d9784-af45-4c73-8feb-e783b7583afb/ESPANHA.jpg)
Caption: (Imagem: FIFA | Reprodução)

**Festa com sangria e paella.** No Estádio Olímpico de Sidney, na Austrália, a Espanha derrotou a Inglaterra e levou pra casa seu [primeiro título da Copa do Mundo Feminina](https://www.cnnbrasil.com.br/esportes/espanha-derrota-inglaterra-e-conquista-primeiro-titulo-da-copa-do-mundo-feminina/?utm_source=thenewscc&utm_medium=email&utm_campaign=referral).

* Aos [28 minutos do primeiro tempo](https://www.cnnbrasil.com.br/esportes/espanha-derrota-inglaterra-e-conquista-primeiro-titulo-da-copa-do-mundo-feminina/?utm_source=thenewscc&utm_medium=email&utm_campaign=referral), a lateral-esquerda Olga Carmona marcou o gol histórico, que garantiu a taça do torneio.

Após a vitória, a Espanha se tornou o segundo país a **ganhar títulos de Copa tanto no masculino quanto no feminino.** Antes disso, [só a Alemanha tinha conquistado esse feito](https://www.cnnbrasil.com.br/esportes/espanha-derrota-inglaterra-e-conquista-primeiro-titulo-da-copa-do-mundo-feminina/?utm_source=thenewscc&utm_medium=email&utm_campaign=referral).

“**Nem tudo foi festa…** O presidente da federação espanhola causou uma cena repugnante na entrega de medalhas, simplesmente dando um [beijo forçado na boca da camisa 10 do time](https://ge.globo.com/futebol/copa-do-mundo-feminina/noticia/2023/08/20/jenni-hermoso-da-espanha-leva-beijo-na-boca-durante-entrega-da-taca-da-copa-veja-video.ghtml?utm_source=the%20news&utm_medium=newsletter&utm_campaign=21_08), Jenni Hermoso.“ —

### **O lado financeiro do jogo **💸

Além de levar o troféu pra casa, a seleção espanhola vai receber o prêmio total do torneio, de US$ 15,7 milhões. O valor é 4x maior do que o da edição anterior, em 2019 — e [3x menor ao da Copa masculina de 2022](https://www.poder360.com.br/esportes/selecao-da-espanha-e-campea-da-copa-feminina/?utm_source=thenewscc&utm_medium=email&utm_campaign=referral).

Essa é a 1ª edição da Copa do Mundo Feminina em que todas as jogadoras vão receber **pagamentos individuais** por participar da competição. Cada atleta da equipe vencedora leva pra casa [US$ 270 mil](https://www.poder360.com.br/esportes/selecao-da-espanha-e-campea-da-copa-feminina/?utm_source=thenewscc&utm_medium=email&utm_campaign=referral).

**Não é à toa:** A seleção espanhola é o 2º time mais valioso do torneio, com valor de mercado estimado em € 4 milhões. A equipe da Inglaterra aparece logo em seguida, com € 3,7 milhões.

## **Que tal colocar a IA do seu lado na hora de analisar dados?**

###### **PATROCINADO POR ALURA**

Ver imagem: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/90cfc624-17aa-4088-b861-36e386187f75/unnamed.gif)
Seguir link da imagem: (https://www.alura.com.br/imersao-dados-ia?utm_source=thenews&utm_medium=cpc&utm_campaign=imersao-dados_ia&utm_id=tn_1&utm_content=middle2108)
Caption:

Quando o assunto é **análise de dados**, não basta ler e interpretar, é preciso transformá-los em insights.

* Pensando nisso, a [Alura](https://www.alura.com.br/imersao-dados-ia?utm_source=thenews&utm_medium=cpc&utm_campaign=imersao-dados_ia&utm_id=tn_1&utm_content=middle2108) vai te ajudar a **otimizar seu trabalho** e a potencializar suas análises utilizando ChatGPT e outras ferramentas de Inteligência Artificial.

São **5 aulas gratuitas** que vão melhorar sua performance e habilidade para que você possa aplicá-las em qualquer área — seja em BI, marketing, gestão, finanças ou atendimento. Não à toa, a Alura é a [maior escola brasileira de cursos online de tecnologia.](https://www.alura.com.br/imersao-dados-ia?utm_source=thenews&utm_medium=cpc&utm_campaign=imersao-dados_ia&utm_id=tn_1&utm_content=middle2108)

Durante as aulas, você vai descobrir como aplicar tudo que está aprendendo e, ainda, contar com uma comunidade de milhares de profissionais pra aumentar seu networking.

“[É só se inscrever aqui](https://www.alura.com.br/imersao-dados-ia?utm_source=thenews&utm_medium=cpc&utm_campaign=imersao-dados_ia&utm_id=tn_1&utm_content=middle2108) e pronto. 🤓“ —

## **Brasil bate recorde de varejistas faturando mais de R$ 1 bilhão**

###### **ECONOMIA**

Ver imagem: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/21e840cb-26bf-4953-9cdf-2991d8278864/VAREJO_MERCADO.jpg)
Caption: (Foto: Tânia Rêgo | Agência Brasil)

**Clube das bilionárias crescendo.** Mesmo com o mercado ainda se recuperando depois da pandemia, em 2022, o varejo brasileiro aumentou o número de empresas com [faturamento superior a R$ 1 bilhão](https://www.poder360.com.br/economia/173-varejistas-brasileiras-faturaram-mais-de-r-1-bilhao-em-2022/?utm_source=thenewscc&utm_medium=email&utm_campaign=referral).

“Considerando as 300 maiores varejistas do pais, 173 ultrapassam essa marca, [17 a mais do que em 2021](https://www.poder360.com.br/economia/173-varejistas-brasileiras-faturaram-mais-de-r-1-bilhao-em-2022/?utm_source=thenewscc&utm_medium=email&utm_campaign=referral).“ —

Somando o faturamento de todas essas empresas da lista, o valor chega a R$ 1 trilhão, representando uma alta de quase R$ 154 bilhões em relação ao ano anterior. **O** **TOP 10 ficou assim:**

1. **Grupo Carrefour Brasil:** R$ 108 bilhões;

2. **Assaí:** R$ 59,7 bilhões;

3. **Magazine Luiza:** R$ 44,7 bilhões;

4. **Via:** R$ 39 bilhões;

5. **Americanas:** R$ 34,4 bilhões;

6. **Raia Drogasil:** R$ 30,9 bilhões;

7. **Grupo Boticário:** R$ 23,6 bilhões;

8. **Natura&Co:** R$ 20,7 bilhões;

9. **Grupo Mateus:** R$ 20,4 bilhões;

10. **Grupo Pão de Açúcar:** R$ 18,4 bilhões;

Como deu pra perceber pela lista, o principal destaque é o **setor de supermercados**, com [152 representantes](https://www.metropoles.com/negocios/varejo-clube-das-bilionarias-aumenta-mas-regionais-puxam-alta?utm_source=thenewscc&utm_medium=email&utm_campaign=referral) no ranking de maiores varejistas. Em seguida, aparece o setor de moda e calçados, com [38 empresas](https://www.metropoles.com/negocios/varejo-clube-das-bilionarias-aumenta-mas-regionais-puxam-alta?utm_source=thenewscc&utm_medium=email&utm_campaign=referral).

Apesar de não entrar no TOP 5, [o Grupo Boticário é a empresa com mais lojas no Brasil](https://www.metropoles.com/negocios/varejo-clube-das-bilionarias-aumenta-mas-regionais-puxam-alta?utm_source=thenewscc&utm_medium=email&utm_campaign=referral), contando com 3.828 pontos de venda. [Veja o relatório completo aqui](https://static.poder360.com.br/2023/08/ranking-sbvc-2023.pdf).

**Outros destaques em economia:**

* **Campos Neto: **[Reajuste nos preços da gasolina e diesel terá impacto de 0,40 p.p. no IPCA](https://exame.com/economia/campos-neto-afirma-que-reajuste-nos-precos-da-gasolina-e-diesel-tera-impacto-de-040-pp-no-ipca/?utm_source=the%20news&utm_medium=newsletter&utm_campaign=21_08)

* **Lembra disso? **[Seca no Canal do Panamá persiste e já conta com +200 navios esperando para transitar](http://archive.today/2023.08.21-044413/https://valor.globo.com/mundo/noticia/2023/08/20/seca-provoca-congestionamento-de-navio-no-canal-do-panam.ghtml)

* **Aos investidores de plantão: **[Clique aqui se quiser ver o que está no calendário do mercado para esta semana](https://www.infomoney.com.br/mercados/ipca-15-de-agosto-powell-no-jackson-hole-china-e-noticiario-politico-o-que-acompanhar-na-semana/?utm_source=the%20news&utm_medium=newsletter&utm_campaign=21_08)

## **Depois que você experimenta, não dá mais pra abrir mão**

###### **PATROCINADO POR VERDE CAMPO**

Ver imagem: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/f9db3466-da2f-41c4-a2b4-bf0a7126a850/23_08_VC_TheNew__2__1_.gif)
Seguir link da imagem: (https://verdecampo.com.br/)
Caption:

Seja no café da manhã ou lanche da tarde, [os produtos da Verde Campo](https://verdecampo.com.br/) são a sua escolha perfeita para quando você quiser algo **saudável e cheio de sabor.** 🥄

* A marca conta com iogurtes e shakes proteicos e vários outros laticínios — todos produzidos com ingredientes de origem natural.

[Confira aqui as variedades](https://loja.verdecampo.com.br/?utm_source=thenews&utm_medium=email&utm_campaign=THENEWSVC10) e garanta **10% OFF** na compra de qualquer produto usando o cupom _THENEWSVC10_ — limitado por CPF.

*_Entregas disponíveis para SP, região e Campinas._

## Você quer ganhar a canequinha do the news em casa?

###### **PROGRAMA DE INDICAÇÃO**

Assim como +10.000 dos nossos leitores, você pode indicar o nosso jornal e ganhar presentes exclusivos do nosso time. A nossa clássica canequinha, nossos adesivos e nossa mochila estão à sua espera. É só clicar no botão abaixo.

COMPARTILHAR (https://thenews.createsend1.com/t/t-i-aohiik-l-tr/)

**PS: **_E-mails da mesma titularidade (mesmo IP) não serão considerados válidos._

# the news 📬

Mais inteligente em 5 minutos. Somos um jornal gratuito e diário, que tem por objetivo te trazer tudo que você precisa saber para começar o seu dia bem e informado.

Notícias, de fato, relevantes sobre as principais atualidades do mundo, do Brasil, tecnologia e do mercado financeiro, sempre nessa ordem.

Direto na sua caixa de entrada do e-mail favorito, sempre às 06:06. É gratuito, mas pode viciar.

🎟️ O próximo anunciante pode ser você. [É só clicar aqui](https://thenewscc.typeform.com/to/twCcjRb Q).

😀😐☹️ **Quão satisfeito você ficou com essa edição?** [Nos conte aqui](https://forms.gle/9FZQQJ3ff5ymAMxD7).

📱** Quer ser um influenciador do seu jornal favorito? **[Clique aqui para saber mais](https://docs.google.com/forms/d/e/1FAIpQLSd-T2gcMxiJpkPfUnQiuLops8WaAYxvxgyN1JRsBvs66PzOUw/viewform).

## já conhece nossas outras marcas?

🎧 **[the jams](https://www.youtube.com/watch?v=rElLCIiNgec&list=PLeefjnjGUtY5on5iCG4I023XrGqt2xvIH&index=6)****: **músicas legais para dar play e deixar tocando a qualquer momento. sozinho ou bem acompanhado o objetivo é um só: **[elevar a sua frequência](https://www.youtube.com/watch?v=rElLCIiNgec&list=PLeefjnjGUtY5on5iCG4I023XrGqt2xvIH&index=6)****.**

📠** ****[the jobs](https://pingback.com/thejobs/?utm_source=organico&utm_medium=sessao&utm_campaign=recomendacao)****: **tudo que você precisa para se desenvolver profissionalmente e tomar as melhores decisões em sua carreira. **[seu one-on-one favorito.](https://pingback.com/thejobs/?utm_source=organico&utm_medium=sessao&utm_campaign=recomendacao)**

🦄** ****[the bizness](https://thenewscc.com.br/bizness-cadastro/?utm_source=newsletter&utm_medium=orgânico&utm_campaign=sessa-recomendacao)****: **sua dose de conteúdo sobre os assuntos mais relevantes do mundo dos negócios. análises, números e insights. **[um MBA em forma de e-mail.](https://thenewscc.com.br/bizness-cadastro/?utm_source=newsletter&utm_medium=orgânico&utm_campaign=sessa-recomendacao)**

**🏆 ****[the champs](https://thenewscc.com.br/champs-cadastro/?utm_source=newsletter&utm_medium=orgânico&utm_campaign=sessa-recomendacao)****: **todo o não óbvio sobre os esportes, na palma da sua mão. **[descontraído e direto ao ponto, como deve ser](https://thenewscc.com.br/champs-cadastro/?utm_source=newsletter&utm_medium=orgânico&utm_campaign=sessa-recomendacao)**.

🧸** ****[the stories](https://thenewscc.com.br/stories-cadastro/?utm_source=newsletter&utm_medium=o rgânico&utm_campaign=sessa-recomendacao)****: **histórias que emocionam. não tão longas quanto um romance, mas suficientes pra te fazer sentir. **[contamos e escrevemos amor.](https://thenewscc.com.br/stories-cadastro/?utm_source=newsletter&utm_medium=orgânico&utm_campaign=sessa-recomendacao)**

# até amanhã

Sempre chegamos a sua caixa de entrada por volta das 06:06. Alguns servidores de e-mail são teimosos e atrasam… Outros são piores ainda e nos jogam para o spam e/ ou promoções. Sempre que não nos encontrar na caixa de entrada, procure nessas duas.


———

Você está lendo uma versão de texto simples deste post. Para uma melhor experiência, copie e cole este link em seu navegador para ver o post online:
https://thenewscc.beehiiv.com/p/21082023
'''


@Test()
def getCompiledEmailBodyList_newBody():
    #arrange
    expected = [
        'bem e informado.',
        'bom dia. seja bem-vindo ao jornal que te deixa não só bem-informado, mas bem e informado. há uma singela diferença. que seja mais uma belíssima semana.',
        'MUNDO',
        'Ozempic e Wegovy estão inclinando a balança econômica da Dinamarca.',
        'A Dinamarca está vendo a sua economia ser afetada positivamente pela Novo Nordisk, responsável pelos “remédios do momento”, que são usados para diabetes e perda de peso.',
        'O valor de mercado da fabricante do Ozempic e do Wegovy acaba de chegar em US$ 419 bilhões, ultrapassando nada menos que o PIB da Dinamarca, o país de origem da empresa.',
        'Graças às vendas massivas dos medicamentos ao redor do mundo, a moeda local passou por uma valorização em relação ao euro.',
        'Isso fez com que o banco central dinamarquês baixasse as taxas de juros, indo na contramão do movimento mais recente do Banco Central Europeu.',
        '“É bom, mas nem tanto…”',
        'Para um país com apenas 5 milhões de habitantes — metade da Grande São Paulo —, ter uma empresa nacional desempenhando um papel tão desproporcional na economia pode ser arriscado.',
        'A Finlândia, que foi dominada pela Nokia e viu um aumento de 55% no PIB entre 1995 e 2007, teve uma década de estagnação e queda na renda per capita depois do declínio da companhia.',
        'A Novo Nordisk, agora, é a segunda empresa pública mais valiosa da Europa, ficando atrás apenas do conglomerado de luxo LVMH, de propriedade do Bernard Arnault — um dos homens mais ricos do mundo.',
        'O que mais é destaque pelo mundo?',
        f'Após eleições tensas e violentas: Com +90{c.PERCENT} apurado, candidata de esquerda e empresário disputarão 2° turno no Equador.',
        'Xi Jinping não gostou disso: EUA, Japão e Coreia do Sul fazem sua primeira cúpula trilateral.',
        'Furacão Hillary: Depois de passar pelo México, autoridades da Califórnia alertam para inundações com risco de vida.',
        'BRASIL',
        'STF forma maioria para que juízes possam julgar clientes de familiares.',
        'Novidade no mundo jurídico. O Supremo Tribunal Federal formou maioria para permitir que juízes atuem em processos que envolvam clientes de escritórios de advocacia de seus familiares.',
        'A regra atual define que isso não pode acontecer, sob um entendimento de que pode haver algum possível conflito de interesses. Agora, isso deve mudar.',
        'Dando um exemplo real… O antigo escritório de advocacia do novo ministro do Supremo, Cristiano Zanin, que agora é administrado somente por sua esposa, atua em 14 diferentes processos que estão tramitando no STF.',
        'Antes, Zanin ficaria de fora da votação desses processos, por envolver uma parente sua. Com o entendimento da lei mudando, ele fica apto para julgar todos eles.',
        'As justificativas 👨🏻‍⚖️',
        'A ação foi apresentada pela Associação dos Magistrados Brasileiros, que argumentou que é “impossível” para um juiz conhecer todos os processos em que uma empresa é representada por um escritório onde um parente trabalhe.',
        'Na outra ponta, todas as instituições consultadas — incluindo Câmara, Senado e Presidência da República — se opuseram ao pedido, argumentando que o atual impedimento ajuda a manter a imparcialidade dos juízes.',
        'Inclusive, os ministros que têm filhos ou cônjuges na advocacia, como Zanin, Gilmar, Toffoli, Moraes, Fux, Barroso e Fachin, devem ser impactados diretamente com a decisão.',
        'Falando em STF… O Tribunal também formou maioria para manter a decisão do ministro Alexandre de Moraes que proibiu a remoção forçada de pessoas em situação de rua. O pessoal de Brasília trabalhou muito no final de semana. risos.',
        'Além disso, o que mais é destaque por aqui?',
        "'Não recebi nada”. Bolsaro dá entrevista exclusiva comentando o caso das joias e quebra de sigilo determinada por Moraes.",
        'Boletim médico: Faustão, internado há 15 dias, aguarda transplante do coração.',
        'Gerou revolta: 123Milhas cancela pacotes de passagens de sua linha promocional e diz que reembolso será em forma de voucher.',
        'TECNOLOGIA',
        'Cientistas recriam música do Pink Floyd lendo sinais cerebrais de ouvintes.',
        '“We don’t need no education”. Depois de treinar um computador para analisar a atividade cerebral em reação à música, foi reproduzida uma versão abafada desse clássico do Pink Floyd.',
        'Usando a inteligência artificial a partir das ondas cerebrais dos ouvintes, esse foi o primeiro experimento a reconstruir uma música através de sinais neurais.',
        'Como funcionou? Como parte de um tratamento da epilepsia — distúrbio que pode causar convulsões —, alguns pacientes tiveram uma rede de eletrodos implantados em seus cérebros.',
        'Isso criou uma oportunidade para os neurocientistas registrarem a atividade cerebral deles enquanto ouviam música, confirmando ideias antigas sobre os papéis de cada parte do nosso cérebro.',
        'Embora os dois lados trabalhem em conjunto, a linguagem é mais processada pelo lado esquerdo, enquanto a música é “mais distribuída, com viés pra direita”.',
        'A relevância: Essas descobertas oferecem um primeiro passo significativo para a criação de dispositivos que ajudem as pessoas que não conseguem falar.',
        'Isso porque, ao entender melhor como o cérebro processa a música, os cientistas não conseguem apenas reconstruir palavras isoladas, mas também o ritmo, a entonação e a emoção da fala.',
        '🤔 Por que Pink Floyd? A equipe escolheu a música, em parte, porque os pacientes mais velhos gostaram dela. Além disso, seus 41 segundos de letra e 2 minutos e meio de instrumentos ajudaram na diferenciação de palavras versus melodia.',
        'THE JOBS',
        'Quanto você pagaria em uma newsletter quinzenal?',
        'Pergunta errada. Na verdade, quanto você pagaria para poder desenvolver sua carreira, ser percebido pelo seu gestor, conseguir manter seu time alinhado, ter acesso a frameworks para situações difíceis do dia a dia do mundo corporativo…',
        'Quanto você pagaria para ter alguém que já tem experiência no mercado respondendo as suas perguntas de maneira personalizada sobre os dilemas do seu atual momento?',
        'Não… Não precisa arrastar pra cima e assinar uma masterclass ou uma mentoria com um desses gurus da internet.',
        'A ideia do the jobs é trazer cada um desses pontos em um formato simples e objetivo, que seja agradável de consumir — exatamente no estilo the news que você já conhece bem.',
        "Não prometemos que seu salário vai aumentar em tantas vezes em apenas um mês, ou que você será promovido em tempo recorde! Não fazemos mágica, e o 'trabalho sujo' continuará sendo seu.",
        'Mas, fornecendo ferramentas, exercícios, conselhos práticos, dicas, insights e algumas boas histórias, faremos de tudo para te impulsionar ao seu objetivo de se destacar na carreira.',
        'ESPORTE',
        'Espanha é campeã da Copa Feminina e embolsa US$ 16 mi.',
        'Festa com sangria e paella. No Estádio Olímpico de Sidney, na Austrália, a Espanha derrotou a Inglaterra e levou pra casa seu primeiro título da Copa do Mundo Feminina.',
        'Aos 28 minutos do primeiro tempo, a lateral-esquerda Olga Carmona marcou o gol histórico, que garantiu a taça do torneio.',
        'Após a vitória, a Espanha se tornou o segundo país a ganhar títulos de Copa tanto no masculino quanto no feminino. Antes disso, só a Alemanha tinha conquistado esse feito.',
        'Nem tudo foi festa… O presidente da federação espanhola causou uma cena repugnante na entrega de medalhas, simplesmente dando um beijo forçado na boca da camisa 10 do time, Jenni Hermoso.',
        'O lado financeiro do jogo 💸',
        'Além de levar o troféu pra casa, a seleção espanhola vai receber o prêmio total do torneio, de US$ 15,7 milhões. O valor é 4x maior do que o da edição anterior, em 2019 — e 3x menor ao da Copa masculina de 2022.',
        'Essa é a 1ª edição da Copa do Mundo Feminina em que todas as jogadoras vão receber pagamentos individuais por participar da competição. Cada atleta da equipe vencedora leva pra casa US$ 270 mil.',
        'Não é à toa: A seleção espanhola é o 2º time mais valioso do torneio, com valor de mercado estimado em € 4 milhões. A equipe da Inglaterra aparece logo em seguida, com € 3,7 milhões.',
        'ECONOMIA',
        'Brasil bate recorde de varejistas faturando mais de R$ 1 bilhão.',
        'Clube das bilionárias crescendo. Mesmo com o mercado ainda se recuperando depois da pandemia, em 2022, o varejo brasileiro aumentou o número de empresas com faturamento superior a R$ 1 bilhão.',
        'Considerando as 300 maiores varejistas do pais, 173 ultrapassam essa marca, 17 a mais do que em 2021.',
        'Somando o faturamento de todas essas empresas da lista, o valor chega a R$ 1 trilhão, representando uma alta de quase R$ 154 bilhões em relação ao ano anterior. O TOP 10 ficou assim:',
        '1. Grupo Carrefour Brasil: R$ 108 bilhões;',
        '2. Assaí: R$ 59,7 bilhões;',
        '3. Magazine Luiza: R$ 44,7 bilhões;',
        '4. Via: R$ 39 bilhões;',
        '5. Americanas: R$ 34,4 bilhões;',
        '6. Raia Drogasil: R$ 30,9 bilhões;',
        '7. Grupo Boticário: R$ 23,6 bilhões;',
        '8. Natura and Co: R$ 20,7 bilhões;',
        '9. Grupo Mateus: R$ 20,4 bilhões;',
        '10. Grupo Pão de Açúcar: R$ 18,4 bilhões;',
        'Como deu pra perceber pela lista, o principal destaque é o setor de supermercados, com 152 representantes no ranking de maiores varejistas. Em seguida, aparece o setor de moda e calçados, com 38 empresas.',
        'Apesar de não entrar no TOP 5, o Grupo Boticário é a empresa com mais lojas no Brasil, contando com 3.828 pontos de venda. Veja o relatório completo aqui.',
        'Outros destaques em economia:',
        'Campos Neto: Reajuste nos preços da gasolina e diesel terá impacto de 0,40 p.p. no IPCA.',
        'Lembra disso? Seca no Canal do Panamá persiste e já conta com +200 navios esperando para transitar.'
    ]

    #act
    toAssert = EmailStaticHelper.getCompiledEmailBodyList(NEW_BODY)

    #assert
    for e, t in zip(expected, toAssert):
        assert ObjectHelper.equals(e, t), f'{e} == {t}'


WEIRD_OPEN_CLOSE_COLON_THING = '''“Considerando as 300 maiores varejistas do pais, 173 ultrapassam essa marca, [17 a mais do que em 2021]. “ —
“Embora os dois lados trabalhem em conjunto, a linguagem é mais processada pelo lado esquerdo, enquanto a música é_ [“mais distribuída, com viés pra direita”]_ “ —'''


@Test()
def getCompiledEmailBodyList_weirdOpenColonCloseColonThing():
    #arrange
    expected = [
        'Considerando as 300 maiores varejistas do pais, 173 ultrapassam essa marca, 17 a mais do que em 2021.', 
        'Embora os dois lados trabalhem em conjunto, a linguagem é mais processada pelo lado esquerdo, enquanto a música é “mais distribuída, com viés pra direita”'
    ]

    #act
    toAssert = EmailStaticHelper.getCompiledEmailBodyList(WEIRD_OPEN_CLOSE_COLON_THING)

    #assert
    assert ObjectHelper.isNotEmpty(toAssert)
    assert ObjectHelper.equals(expected, toAssert), f'{expected} == {toAssert}'


INDEX_ERROR_NEW_BODY = '''Ver imagem: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/064b9cc2-fde8-45c0-b0c1-d226907b693c/US_CRANBERRIES.png)
Seguir link da imagem: (https://www.coderhouse.com.br/?utm_source=thenews&utm_medium=cpc&utm_campaign=)
Caption:

##### **back on track**

##### bom dia. depois do feriado, é hora de voltar à rotina e fazer o que tem que ser feito. que seja mais uma bela semana. let’s go!

Ver imagem: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/b8b1d4ec-53c6-4348-b78a-ec8df3b25302/MAIS_INTELIGENTE_EM_5_MINUTOS.png)
Caption:

#####
**Terremoto em Marrocos, brasileiro fugitivo e G20**

##### **MUNDO**

Ver imagem: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/0d58d846-f19d-4798-b087-9902e6defd27/image__61_.jpeg)
Caption: (Imagem: O Globo | Reprodução)

🏥** Tragédia.** Com magnitude de 6,8, o terremoto que atingiu Marrocos na sexta-feira causou mais de 2 mil mortes e é o mais forte já registrado para a região em pelo menos 120 anos. [Seu impacto equivale a 32 bombas atômicas lançadas em Hiroshima durante a 2ª Guerra Mundial](https://www.poder360.com.br/internacional/terremoto-no-marrocos-equivale-a-32-bombas-atomicas/).

**🌎 18ª Cúpula do G20.** A reunião terminou com um texto vago sobre a guerra da Ucrânia, sem responsabilizar a Rússia, e algumas discussões sobre o enfrentamento das questões climáticas. Nas discussões geopolíticas, o discurso do Lula — [que assumiu a presidência](https://www.cnnbrasil.com.br/internacional/brasil-assume-presidencia-do-g20-e-lula-diz-que-geopolitica-nao-pode-sequestrar-agenda-do-bloco/) — se aproximou mais da linha adotada pela China e pela Rússia, e menos da Europa e dos EUA.

👀** No flagra.** Danelo Cavalcante, brasileiro foragido nos EUA, foi visto no sábado de “aparência renovada”. Sua fuga escalando o muro da prisão aconteceu depois dele ter sido condenado pelo assassinato de seu ex-namorada em 2021. [As buscas 24/7 em uma operação de quase 400 policiais continuam.](https://www.cnnbrasil.com.br/internacional/assassino-brasileiro-foragido-nos-eua-e-visto-a-noite-de-aparencia-renovada/?utm_source=thenewscc&utm_medium=email&utm_campaign=referral)

———————————————————————————

##### **Prejuízos com ciclone no Sul somam R$ 1,3 bilhão**

##### **BRASIL**

Ver imagem: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/3533bca5-862c-4146-879c-723dd729ee6e/image__62_.jpeg)
Caption: (Imagem: g1 | Reprodução)

**Tragédia.** No Rio Grande do Sul, [88 municípios](https://www.cnnbrasil.com.br/nacional/numero-de-mortos-por-chuvas-no-rio-grande-do-sul-sobe-para-42/) foram devastados pelas chuvas que deixaram mais de 11 mil pessoas desabrigadas ou desalojadas — em abrigos públicos ou se acomodando na casa de amigos e parentes.

* Até então, foram registradas [43 mortes](https://www.cnnbrasil.com.br/nacional/numero-de-mortos-por-chuvas-no-rio-grande-do-sul-sobe-para-42/) no estado, sendo que 46 pessoas estão desaparecias.

Ao todo, estima-se que [150 mil habitantes](https://www.poder360.com.br/brasil/prejuizos-com-ciclone-no-sul-somam-r-13-bilhao/) foram afetados pelos temporais, o que levou o governo a impor uma força-tarefa de 900 servidores atuando nas buscas, resgates e reparação de estrutura.

**Impactos econômicos:** O ciclone extratropical já causou prejuízos de R$ 1,3 bilhão, com a maior parte das perdas registradas nos **comércios locais.** [A agriculta e a pecuária apareceram em segundo e terceiro lugar](https://www.poder360.com.br/brasil/prejuizos-com-ciclone-no-sul-somam-r-13-bilhao/).

“Em relação ao **setor público**, já foram R$ 26 milhões em prejuízos, com mais de R$ 20 milhões no setor de transportes. Na sequência, aparecem a limpeza urbana e assistência médica.“ —

Como o Lula está na Índia para a cúpula do G20, quem visitou o estado foi o vice-presidente, Geraldo Alckmin, anunciando o repasse de [R$ 741 milhões](https://g1.globo.com/rs/rio-grande-do-sul/noticia/2023/09/10/governo-federal-anuncia-recursos-para-cidades-atingidas-por-ciclone-no-rs.ghtml) para as cidades atingidas.

O ministro do Desenvolvimento Social, Wellington Dias, também afirmou que o governo vai disponibilizar [R$ 56 milhões](https://www.poder360.com.br/brasil/governo-disponibilizara-r-56-mi-para-vitimas-de-ciclone-no-sul/) de vários programas sociais da pasta às famílias afetadas pelo desastre.

**O que mais é destaque pelo nosso país? **

* **Superou o Rei:** _[Neymar se consagra como o maior artilheiro da história da Seleção](https://ge.globo.com/google/amp/futebol/selecao-brasileira/noticia/2023/09/08/neymar-supera-pele-e-se-torna-o-maior-artilheiro-da-selecao-brasileira-nas-contas-da-fifa.ghtml?utm_source=the%20news&amp;utm_medium=newsletter&amp;utm_campaign=11_09)_

* **He is back:** _[Faustão recebe alta hospitalar após transplante de coração](https://agenciabrasil.ebc.com.br/geral/noticia/2023-09/faustao-recebe-alta-hospitalar-apos-transplante-de-coracao?utm_source=the%20news&amp;utm_medium=newsletter&amp;utm_campaign=11_09)_

* **Já que falamos do G20:** _[Lula fala que não prenderia Putin caso ele viesse ao Brasil, o que violaria o Estatuto de Roma](https://noticias.uol.com.br/colunas/jamil-chade/2023/09/10/lula-violaria-haia-se-nao-prender-putin-e-caso-iria-a-conselho-de-seguranca.htm?utm_source=the%20news&amp;utm_medium=newsletter&amp;utm_campaign=11_09)_

* **Depois de 4 meses:** _[Mauro Cid deixa a prisão após Moraes homologar delação premiada](https://www.terra.com.br/amp/noticias/brasil/politica/mauro-cid-deixa-a-prisao-apos-moraes-homologar-delacao-premiada,ea767618958d7a2582abe5255756164djd18vyw1.html?utm_source=the%20news&amp;utm_medium=newsletter&amp;utm_campaign=11_09)_

———————————————————————————

## **O novo celular da Huawei pode virar problema geopolítico  **

###### **TECNOLOGIA**

Ver imagem: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/5d6c850e-ee6b-44af-bcbf-ac97ba80e9d1/mate60pro-huawei.jpg)
Caption: (Imagem: James Park | Bloomberg)

A empresa chinesa Huawei [lançou seu mais novo celular](https://www.reuters.com/technology/chinas-huawei-launches-mate-60-pro-smartphone-presale-2023-09-08/?utm_source=the%20news&utm_medium=newsletter&utm_campaign=11_09) na semana passada. Desde então, um **burburinho tem tomado conta do mundo da tecnologia**, e também no ambiente **geopolítico.**

**Explicando…** O Mate 60 Pro da Huawei tem velocidade superior aos aos dispositivos 5G de primeira linha e parece [rodar em um microchip de ponta fabricado na China](https://epocanegocios.globo.com/tecnologia/noticia/2023/09/huawei-lanca-smartphone-mate-60-pro-em-novo-avanco-contra-sancoes-dos-eua.ghtml?utm_source=the%20news&utm_medium=newsletter&utm_campaign=11_09).

Isso surpreendeu toda a indústria, que não acreditava que o país asiático tinha capacidade de **produzir um semicondutor tão avançado.**

* **Abre parêntese:** Esses chips são peças-chave para todo o sistema e corrente elétricos de dispositivos, desde AIs até geladeiras.

**Por que essa conversa importa?** Nos últimos quatro anos os EUA têm imposto [restrições de exportação para o dificultar o acesso da China](https://www.wsj.com/articles/u-s-goes-full-court-press-on-chinas-chip-sector-11665403410) à tecnologia — citando temores sobre o uso dos militares do país.

Mesmo assim, o gigante asiático conseguiu chegar a uma produção própria. Agora, o governo americano suspeita que a companhia tenha violado as sanções impostas por ele. **Chances de farpas diplomáticas.**

Enquanto alguns americanos defendem aumento das restrições à China, outros dizem que aumentar as sanções é um estímulo para o país virar autossuficiente, sem mais depender de importações de chips.

**Tirando o zoom:** O novo celular da Huawei está [vendendo como água na China](https://www.digitimes.com/news/a20230905PD211/china-huawei-mobile-devices.html?utm_source=the%20news&utm_medium=newsletter&utm_campaign=11_09), ameaçando a forte presença da Apple, que tem [20%](https://www.seudinheiro.com/2023/internacional/apple-china-acoes-restricoes-iphone-vinp/?utm_source=the%20news&utm_medium=newsletter&utm_campaign=11_09) das suas vendas alocadas no país.

🍎🇨🇳 **Falando nisso…** A maçã perdeu [US$ 200 bilhões](https://forbes.com.br/forbes-tech/2023/09/  por-que-us-74-bilhoes-de-receita-da-apple-estao-em-risco/?utm_source=the%20news&utm_medium=newsletter&utm_campaign=11_09) de seu valor de mercado na semana passada, depoisue o governo chinês proibiu parte de seus funcionários e autoridades de usar iPhones.

———————————————————————————

## **Seu plano para dominar o mundo começa aqui **🎯

###### **PATROCINADO POR CODERHOUSE **

Ver imagem: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/623a38a9-0697-495a-b4ee-6fe46e31fa24/40F504FF-F5E7-44F5-989A-BA019C5C04EF.gif)
Seguir link da imagem: (https://www.coderhouse.com.br/?utm_source=thenews&utm_medium=cpc&utm_campaign=)
Caption:

O primeiro passo para que seu plano funcione é ter acesso à _[maior comunidade de aprendizagem online e ao vivo da América Latina](https://www.coderhouse.com.br/?utm_source=thenews&utm_medium=cpc&utm_campaign=)_. Mas calma que, para isso, você não precisa de um esquema mirabolante.

É só aproveitar o **Dia do Cliente** na _[Coderhouse](https://www.coderhouse.com.br/?utm_source=thenews&utm_medium=cpc&utm_campaign=)_. Eles liberaram descontos de **até 70% em todos os cursos** e carreiras nas áreas de Design, Programação, Dados, Produto e Marketing Digital. Só hoje você pode:

🖥️ Aproveitar aulas online e ao vivo com especialistas das maiores empresas do mercado, como: OLX,  Nubank e MadeiraMadeira.

📌 Viver o mercado na prática com desafios e cases.


📂 Construir um portfólio de destaque.

👥 Ter acesso a networking com pessoas do mercado digital e muito mais.

Com a Coderhouse, agora você pode garantir tudo isso por um preço acessível e sem precisar abrir mão da qualidade, com parcelas **a partir de 12x de R$ 24,00.**

Para os nossos leitores tudo só fica melhor… Usando cupom _THENEWS,_ você ganha **mais 15% OFF** pra garantir sua vaga hoje, é só _[clicar aqui.](https://www.coderhouse.com.br/?utm_source=thenews&utm_medium=cpc&utm_campaign=)_

———————————————————————————

## **Você já se perguntou isso também**

###### **AD DOS ADS**

Muita gente nos pergunta por que escolhemos o e-mail como nosso canal oficial, comentando que ele está em baixa atualmente. Que nada…

**+4,3 bilhões** de usuários no mundo (mais que WhatsApp e Instagram somados)
**+100 milhões** de usuários novos por ano;
**+3 milhões** de e-mails enviados por segundo;
**+95%** dos usuários checam suas caixas de entrada todos os dias;

**A sua empresa aproveita esse potencial? **_[Clique aqui para entender do que estamos falando](https://thenews-anunciantes.my.canva.site/)_. 📬

———————————————————————————

## **Google vai enfrentar julgamento decisivo sobre monopólio digital**

###### **NEGÓCIOS**

Ver imagem: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/6f7ff42b-e431-4177-883d-503097e9c5ec/image__63_.jpeg)
Caption: (Imagem: Annelise Capossela | Axios)

Na terça-feira, o Google e a sua controladora, Alphabet, estarão diante do julgamento mais importante sobre práticas de **monopólio digital** desde o [caso antitruste aberto contra a Microsoft em 1998](https://www.migalhas.com.br/depeso/225953/o-caso-u-s--v--microsoft--bases-da-relacao-entre-direito-e-tecnologia-da-informacao).

* Na ocasião, o Tribunal acusou a empresa do Bill Gates de exigir que todos os seus computadores fossem equipados com o navegador Internet Explorer.

Como resultado, um juiz determinou que a empresa acabasse com essa restrição, abrindo espaço para o sucesso de vários outros navegadores concorrentes — inclusive o Google.

**O que está acontecendo agora?** A ação contra a empresa da Alphabet, apresentada pela primeira vez em 2020, afirma que o Google [abusou ilegalmente](https://www.nytimes.com/2023/09/06/technology/modern-internet-first-monopoly-trial-us-google-dominance.html?utm_source=thenewscc&utm_medium=email&utm_campaign=referral) do seu poder de mercado como mecanismo de busca.

“Segundo o Departamento de Justiça, isso teria **limitado a concorrência**, “sufocado” a inovação e violado a privacidade dos usuários.“ —

### **Por que isso é importante?**

A disputa judicial atinge o **império de US$ 1,7 trilhão da Alphabet** e pode tirar o poder de influência de uma das empresas mais bem-sucedidas do mundo.

Além disso, por acusar o Google de ter feito acordos com fabricantes de celulares — [como Apple e Samsung](https://www.nytimes.com/2023/09/06/technology/modern-internet-first-monopoly-trial-us-google-dominance.html?utm_source=thenewscc&utm_medium=email&utm_campaign=referral]) — para ser o **mecanismo de busca padrão**, o resultado da ação deve ter um efeito cascata sobre outras gigantes.

👀 O Google acumula atualmente cerca de 90% do mercado de buscas no mundo.

———————————————————————————

## **Hoje não é uma segunda-feira qualquer**

###### **PATROCINADO POR ****KINVO**

Ver imagem: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/364ea9c8-68b3-4954-9f59-582062aab5e0/Design_sem_nome__1___1_-min.gif)
Seguir link da imagem: (https://assine.kinvo.com.br/checkout?cupom=45-OFF-EXCLUSIVOTHENEWS&utm_source=thenews&utm_medium=email&utm_campaign=aniversario-kinvo&utm_content=450ff-exclusivo-thenews)
Caption:

Talvez você tenha acordado, como todo bom dia de trabalho, pensando em como tirar do papel aquela viagem para o exterior, a compra do próprio apê ou, simplesmente, como fazer o seu $ render mais.

🍾 Massss, entramos, hoje, na **Semana do Cliente** e, por isso, o Kinvo preparou uma oportunidade única para você conquistar novos sonhos, [economizando ainda mais.](https://assine.kinvo.com.br/checkout?cupom=45-OFF-EXCLUSIVOTHENEWS&utm_source=thenews&utm_medium=email&utm_campaign=aniversario-kinvo&utm_content=450ff-exclusivo-thenews)


O Kinvo é uma plataforma onde você pode **acompanhar os seus investimentos.** Com recursos avançados, análises detalhadas e uma interface intuitiva, você tem o que precisa para tomar as melhores decisões financeiras.

“[Aproveite os 45% de desconto](https://assine.kinvo.com.br/checkout?cupom=45-OFF-EXCLUSIVOTHENEWS&utm_source=thenews&utm_medium=email&utm_campaign=aniversario-kinvo&utm_content=450ff-exclusivo-thenews) na assinatura do plano, exclusivo para os leitores do the news — **mas somente hoje.**“ —

———————————————————————————

## **Os royalties dos Beatles e Bruno Mars valem US$ 500 mi**

###### **ECONOMIA**

Ver imagem: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/0c42abc6-1d74-4fc4-a30f-e32cbee80763/bruno-mars-1.jpg)
Caption: (Imagem: Manuela Scarpa | Brazil News)

Sabe aquela escolha ousada que todo mundo considera uma ideia maluca? Então, quando John Gruss saiu do banco de investimentos [The Bear Stearns](https://www.bloomberg.com/news/articles/2023-09-08/bear-stearns-analyst-turned-music-mogul-eyes-15-million-payday?srnd=premium-europe#xj4y7vzkg) para investir em **portfólios musicais** seus pais devem ter pensado isso.

* Porém, nesse caso, depois da saída, o banco entrou em falência e foi comprado pelo JP Morgan por cerca de [10% de seu valor de mercado](https://en.wikipedia.org/wiki/Bear_Stearns).

Do outro lado, o seu fundo musical **Round Hill Music Royalty** — que contém mais de 120 mil músicas — foi adquirido pela **Alchemy Copyrights LLC** pelo valor “singelo” de US$ 469 milhões.

* Esse valor se explica quando olhamos para o portfólio do fundo: desde “_She Loves You_”, dos Beatles a outros mais recentes, como “_Marry M_e” e “_Just the Way You Are_”, de Bruno Mars, e “_Fuck You_”, do Cee-Lo Green.

**Como funciona isso?** Investir em Royalties Musicais é lucrar a cada vez que uma música toca no Spotify, Youtube, Apple Music, shows, academias, supermercados, entre outros inúmeros locais.

No caso, são ativos reais vinculados ao desempenho da música — quanto mais ela toca, maior é a rentabilidade. Por exemplo, os compositores de Evidências devem [fazer R$ 2 mil](https://www.instagram.com/p/CxBsS-bITGo/?igshid=MzRlODBiNWFlZA==) (x2) pela banda do Bruno Mars ter tocado o hit no The Town.

“Só pra ter ideia do tamanho do mercado, no Brasil, em 2021, foi faturado mais de [R$ 1 bilhão](https://www.cnnbrasil.com.br/economia/royalties-musicais-podem-ser-opcao-para-diversificar-carteira-veja-como-funciona/) em royalties musicais — **número 20% superior ao de 2020.**“ —

Voltando ao caso, a participação de pouco mais de 3% de John Gruss no **Round Hill Music Royalty**, que ele fundou em 2010, vai lhe garantir pelo menos US$ 15 milhões depois da aquisição do fundo.

**Outros destaques em economia:**

* **O próximo IPO? **_[Instacart visa avaliação de cerca de US$ 9 bi em IPO, bem abaixo do que anteriormente](https://www.cnbc.com/2023/09/10/instacart-aiming-for-valuation-of-8point6-billion-to-9point3-billion-in-ipo-reports.html)_

* **Aos investidores de plantão:** _[IPCA, inflação nos EUA e juros na Europa devem movimentar a semana](https://www.infomoney.com.br/mercados/ipca-inflacao-nos-estados-unidos-e-decisao-de-juros-na-europa-o-que-acompanhar-na-semana/?utm_source=the%20news&amp;utm_medium=newsletter&amp;utm_campaign=11_09)_

———————————————————————————

## **A festa tá bombando, melhor não chegar tarde 🏃🏽♀️ **

###### **PATROCINADO POR MAGALU**

Ver imagem: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/eb4822fe-9cf5-4a7e-8b74-9b4d68222c4f/1600x600_niver__1_.gif)
Seguir link da imagem: (https://www.magazineluiza.com.br/selecao/0309aniversariomagalu/?&banner_id=promoh1md1esporte80off?partner_id=73835&utm_campaign=aniversario_magalu_thenews&utm_source=the_news&utm_medium=display&utm_content=the_news_footer&utm_term=73835)
Caption:

Para comemorar o aniversário do [Magalu](https://www.magazineluiza.com.br/selecao/0309aniversariomagalu/?&banner_id=promoh1md1esporte80off?partner_id=73835&utm_campaign=aniversario_magalu_thenews&utm_source=the_news&utm_medium=display&utm_content=the_news_footer&utm_term=73835), eles liberaram ofertas de **até 80% de desconto** no seu aplicativo e nas lojas físicas. 🛒

**Tem no Magalu.** Produtos de beleza, smartphones, eletrodomésticos, tudo pra sua casa e muitos mais. [Baixe o app, monte o seu carrinho](https://www.magazineluiza.com.br/selecao/0309aniversariomagalu/?&banner_id=promoh1md1esporte80off?partner_id=73835&utm_campaign=aniversario_magalu_thenews&utm_source=the_news&utm_medium=display&utm_content=the_news_footer&utm_term=73835) e aproveite que a entrega é rápida — piscou chegou.

———————————————————————————

## **Isso vai ser útil aos que emendaram o feriadão **

###### **IN CASE YOU MISSED IT**

🚫 **Anulou geral:** [Toffoli anula caso da Odebrecht e diz que prisão do Lula foi armação](https://thenewscc.com.br/brasil/toffoli-anula-caso-da-odebrecht-e-diz-que-prisao-do-lula-foi-armacao/)

🎙️ **Pouco lucrativo?** [O investimento de US$ 1 bi do Spotify em podcasts está dando prejuízo](htt ps://thenewscc.com.br/negocios/os-podcasts-estao-dando-menos-resultados-que-o-spotify-esperava/)

🚗 **Por essa você não esperava…** [Carro é o produto que mais te rastreia — sim, mais que seu Apple Watch](https://thenewscc.com.br/tecnologia/seu-carro-te-rastreia-mais-que-seu-apple-watch/)


🇲🇽 **Oficial, muchacho:** [A Suprema Corte do México legalizou o aborto em todo o país](https://thosenewscc.com.br/mundo/suprema-corte-do-mexico-legaliza-o-aborto-em-todo-o-pais/)

🍫 **Deal chocólatra:** [Nestlé compra Kopenhagen por singelos R$ 3 bilhões](https://thenewscc.com.br/bizness/o-doce-sabor-de-um-deal-bilionario-%f0%9f%8d%ab/)

———————————————————————————

## **Você pode ganhar prêmios caso torne seus amigos leitores**

###### **PROGRAMA DE INDICAÇÃO**

**Indicou, ganhou.** Nosso programa de indicação funciona assim. Quanto mais amigos você trouxer ao clube dos que acordam bem e informados, mais presentes você recebe da nossa equipe.** Clique no botão abaixo:**

COMPARTILHAR (https://thenews.createsend1.com/t/t-i-aohiik-l-tr/)

**PS: **_E-mails da mesma titularidade (mesmo IP) não serão considerados válidos._

———————————————————————————

# the news 📬

Mais inteligente em 5 minutos. Somos um jornal gratuito e diário, que tem por objetivo te trazer tudo que você precisa saber para começar o seu dia bem e informado.

Notícias, de fato, relevantes sobre as principais atualidades do mundo, do Brasil, tecnologia e do mercado financeiro, sempre nessa ordem.

Direto na sua caixa de entrada do e-mail favorito, sempre às 06:06. É gratuito, mas pode viciar.

🎟️ O próximo anunciante pode ser você. [É só clicar aqui](https://thenewscc.typeform.com/to/twCcjRb Q).

😀😐☹️ **Quão satisfeito você ficou com essa edição?** [Nos conte aqui](https://forms.gle/9FZQQJ3ff5ymAMxD7).

📱** Quer ser um influenciador do seu jornal favorito? **[Clique aqui para saber mais](https://docs.google.com/forms/d/e/1FAIpQLSd-T2gcMxiJpkPfUnQiuLops8WaAYxvxgyN1JRsBvs66PzOUw/viewform).

## já conhece nossas outras marcas?

📠** ****[the jobs](https://pingback.com/thejobs/?utm_source=organico&utm_medium=sessao&utm_campaign=recomendacao)****: **tudo que você precisa para se desenvolver profissionalmente e tomar as melhores decisões em sua carreira. **[seu one-on-one favorito.](https://pingback.com/thejobs/?utm_source=organico&utm_medium=sessao&utm_campaign=recomendacao)**

🦄** ****[the bizness](https://thenewscc.com.br/bizness-cadastro/?utm_source=newsletter&utm_medium=orgânico&utm_campaign=sessa-recomendacao)****: **sua dose de conteúdo sobre os assuntos mais relevantes do mundo dos negócios. análises, números e insights. **[um MBA em forma de e-mail.](https://thenewscc.com.br/bizness-cadastro/?utm_source=newsletter&utm_medium=orgânico&utm_campaign=sessa-recomendacao)**

**🏆 ****[the champs](https://thenewscc.com.br/champs-cadastro/?utm_source=newsletter&utm_medium=orgânico&utm_campaign=sessa-recomendacao)****: **todo o não óbvio sobre os esportes, na palma da sua mão. **[descontraído e direto ao ponto, como deve ser](https://thenewscc.com.br/champs-cadastro/?utm_source=newsletter&utm_medium=orgânico&utm_campaign=sessa-recomendacao)**.

🧸** ****[the stories](https://thenewscc.com.br/stories-cadastro/?utm_source=newsletter&utm_medium=o rgânico&utm_campaign=sessa-recomendacao)****: **histórias que emocionam. não tão longas quanto um romance, mas suficientes pra te fazer sentir. **[contamos e escrevemos amor.](https://thenewscc.com.br/stories-cadastro/?utm_source=newsletter&utm_medium=orgânico&utm_campaign=sessa-recomendacao)**

🎧 **[the jams](https://www.youtube.com/watch?v=rElLCIiNgec&list=PLeefjnjGUtY5on5iCG4I023XrGqt2xvIH&index=6)****: **músicas legais para dar play e deixar tocando a qualquer momento. sozinho ou bem acompanhado o objetivo é um só: **[elevar a sua frequência](https://www.youtube.com/watch?v=rElLCIiNgec&list=PLeefjnjGUtY5on5iCG4I023XrGqt2xvIH&index=6)****.**

# até amanhã

Sempre chegamos a sua caixa de entrada por volta das 06:06. Alguns servidores de e-mail são teimosos e atrasam… Outros são piores ainda e nos jogam para o spam e/ ou promoções. Sempre que não nos encontrar na caixa de entrada, procure nessas duas.


———

Você está lendo uma versão de texto simples deste post. Para uma melhor experiência, copie e cole este link em seu navegador para ver o post online:
https://thenewscc.beehiiv.com/p/11092023'''


@Test()
def getCompiledEmailBodyList_indexError_newBody():
    #arrange
    expected = [
        'back on track.',
         'bom dia. depois do feriado, é hora de voltar à rotina e fazer o que tem que ser feito. que seja mais uma bela semana. let’s go!',
         'MUNDO',
         'Terremoto em Marrocos, brasileiro fugitivo e G20.',
         '🏥 Tragédia.',
         'Com magnitude de 6,8, o terremoto que atingiu Marrocos na sexta-feira causou mais de 2 mil mortes e é o mais forte já registrado para a região em pelo menos 120 anos.',
         'Seu impacto equivale a 32 bombas atômicas lançadas em Hiroshima durante a 2ª Guerra Mundial.',
         '🌎 18ª Cúpula do G20.',
         'A reunião terminou com um texto vago sobre a guerra da Ucrânia, sem responsabilizar a Rússia, e algumas discussões sobre o enfrentamento das questões climáticas.',
         'Nas discussões geopolíticas, o discurso do Lula — que assumiu a presidência — se aproximou mais da linha adotada pela China e pela Rússia, e menos da Europa e dos EUA.',
         '👀 No flagra.',
         'Danelo Cavalcante, brasileiro foragido nos EUA, foi visto no sábado de “aparência renovada”.',
         'Sua fuga escalando o muro da prisão aconteceu depois dele ter sido condenado pelo assassinato de seu ex-namorada em 2021.',
         'As buscas 24/7 em uma operação de quase 400 policiais continuam.',
         'BRASIL',
         'Prejuízos com ciclone no Sul somam R$ 1,3 bilhão.',
         'Tragédia. No Rio Grande do Sul, 88 municípios foram devastados pelas chuvas que deixaram mais de 11 mil pessoas desabrigadas ou desalojadas — em abrigos públicos ou se acomodando na casa de amigos e parentes.',
         'Até então, foram registradas 43 mortes no estado, sendo que 46 pessoas estão desaparecias.',
         'Ao todo, estima-se que 150 mil habitantes foram afetados pelos temporais, o que levou o governo a impor uma força-tarefa de 900 servidores atuando nas buscas, resgates e reparação de estrutura.',
         'Impactos econômicos: O ciclone extratropical já causou prejuízos de R$ 1,3 bilhão, com a maior parte das perdas registradas nos comércios locais. A agriculta e a pecuária apareceram em segundo e terceiro lugar.',
         'Em relação ao setor público, já foram R$ 26 milhões em prejuízos, com mais de R$ 20 milhões no setor de transportes. Na sequência, aparecem a limpeza urbana e assistência médica.',
         'Como o Lula está na Índia para a cúpula do G20, quem visitou o estado foi o vice-presidente, Geraldo Alckmin, anunciando o repasse de R$ 741 milhões para as cidades atingidas.',
         'O ministro do Desenvolvimento Social, Wellington Dias, também afirmou que o governo vai disponibilizar R$ 56 milhões de vários programas sociais da pasta às famílias afetadas pelo desastre.',
         'O que mais é destaque pelo nosso país?',
         'Superou o Rei: Neymar se consagra como o maior artilheiro da história da Seleção.',
         'He is back: Faustão recebe alta hospitalar após transplante de coração.',
         'Já que falamos do G20: Lula fala que não prenderia Putin caso ele viesse ao Brasil, o que violaria o Estatuto de Roma.',
         'Depois de 4 meses: Mauro Cid deixa a prisão após Moraes homologar delação premiada.',
         'TECNOLOGIA',
         'O novo celular da Huawei pode virar problema geopolítico.',
         'A empresa chinesa Huawei lançou seu mais novo celular na semana passada. Desde então, um burburinho tem tomado conta do mundo da tecnologia, e também no ambiente geopolítico.',
         'Explicando… O Mate 60 Pro da Huawei tem velocidade superior aos aos dispositivos 5G de primeira linha e parece rodar em um microchip de ponta fabricado na China.',
         'Isso surpreendeu toda a indústria, que não acreditava que o país asiático tinha capacidade de produzir um semicondutor tão avançado.',
         'Abre parêntese: Esses chips são peças-chave para todo o sistema e corrente elétricos de dispositivos, desde AIs até geladeiras.',
         'Por que essa conversa importa? Nos últimos quatro anos os EUA têm imposto restrições de exportação para o dificultar o acesso da China à tecnologia — citando temores sobre o uso dos militares do país.',
         'Mesmo assim, o gigante asiático conseguiu chegar a uma produção própria. Agora, o governo americano suspeita que a companhia tenha violado as sanções impostas por ele. Chances de farpas diplomáticas.',
         'Enquanto alguns americanos defendem aumento das restrições à China, outros dizem que aumentar as sanções é um estímulo para o país virar autossuficiente, sem mais depender de importações de chips.',
         'Tirando o zoom: O novo celular da Huawei está vendendo como água na China, ameaçando a forte presença da Apple, que tem 20% das suas vendas alocadas no país.',
         '🍎🇨🇳 Falando nisso… A maçã perdeu US$ 200 bilhões de seu valor de mercado na semana passada, depoisue o governo chinês proibiu parte de seus funcionários e autoridades de usar iPhones.',
         'NEGÓCIOS',
         'Google vai enfrentar julgamento decisivo sobre monopólio digital.',
         'Na terça-feira, o Google e a sua controladora, Alphabet, estarão diante do julgamento mais importante sobre práticas de monopólio digital desde o caso antitruste aberto contra a Microsoft em 1998.',
         'Na ocasião, o Tribunal acusou a empresa do Bill Gates de exigir que todos os seus computadores fossem equipados com o navegador Internet Explorer.',
         'Como resultado, um juiz determinou que a empresa acabasse com essa restrição, abrindo espaço para o sucesso de vários outros navegadores concorrentes — inclusive o Google.',
         'O que está acontecendo agora? A ação contra a empresa da Alphabet, apresentada pela primeira vez em 2020, afirma que o Google abusou ilegalmente do seu poder de mercado como mecanismo de busca.',
         'Segundo o Departamento de Justiça, isso teria limitado a concorrência, “sufocado” a inovação e violado a privacidade dos usuários.',
         'Por que isso é importante?',
         'A disputa judicial atinge o império de US$ 1,7 trilhão da Alphabet e pode tirar o poder de influência de uma das empresas mais bem-sucedidas do mundo.',
         'Além disso, por acusar o Google de ter feito acordos com fabricantes de celulares — como Apple e Samsung — para ser o mecanismo de busca padrão, o resultado da ação deve ter um efeito cascata sobre outras gigantes.',
         '👀 O Google acumula atualmente cerca de 90% do mercado de buscas no mundo.',
         'ECONOMIA',
         'Os royalties dos Beatles e Bruno Mars valem US$ 500 mi.',
         'Sabe aquela escolha ousada que todo mundo considera uma ideia maluca? Então, quando John Gruss saiu do banco de investimentos The Bear Stearns para investir em portfólios musicais seus pais devem ter pensado isso.',
         'Porém, nesse caso, depois da saída, o banco entrou em falência e foi comprado pelo JP Morgan por cerca de 10% de seu valor de mercado.',
         'Do outro lado, o seu fundo musical Round Hill Music Royalty — que contém mais de 120 mil músicas — foi adquirido pela Alchemy Copyrights LLC pelo valor “singelo” de US$ 469 milhões.',
         'Esse valor se explica quando olhamos para o portfólio do fundo: desde “ She Loves You ”, dos Beatles a outros mais recentes, como “ Marry M e” e “ Just the Way You Are ”, de Bruno Mars, e “ Fuck You ”, do Cee-Lo Green.',
         'Como funciona isso? Investir em Royalties Musicais é lucrar a cada vez que uma música toca no Spotify, Youtube, Apple Music, shows, academias, supermercados, entre outros inúmeros locais.',
         'No caso, são ativos reais vinculados ao desempenho da música — quanto mais ela toca, maior é a rentabilidade. Por exemplo, os compositores de Evidências devem fazer R$ 2 mil (x2 pela banda do Bruno Mars ter tocado o hit no The Town.',
         'Só pra ter ideia do tamanho do mercado, no Brasil, em 2021, foi faturado mais de R$ 1 bilhão em royalties musicais — número 20% superior ao de 2020.',
         'Voltando ao caso, a participação de pouco mais de 3% de John Gruss no Round Hill Music Royalty, que ele fundou em 2010, vai lhe garantir pelo menos US$ 15 milhões depois da aquisição do fundo.',
         'Outros destaques em economia:',
         'O próximo IPO? Instacart visa avaliação de cerca de US$ 9 bi em IPO, bem abaixo do que anteriormente.',
         'Aos investidores de plantão: IPCA, inflação nos EUA e juros na Europa devem movimentar a semana.',
         ]

    #act
    toAssert = EmailStaticHelper.getCompiledEmailBodyList(INDEX_ERROR_NEW_BODY)

    #assert
    assert ObjectHelper.isNotEmpty(toAssert)
    for e, t in zip(expected, toAssert):
        assert ObjectHelper.equals(e, t), f'{e} == {t}'
