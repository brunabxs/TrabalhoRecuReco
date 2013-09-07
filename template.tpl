<html>
    <head>
        <style type="text/css">
            * { margin: 0; padding: 0; color: #333; }
            
            body { margin: 5% 10%; font-family: helvetica, arial, sans; }
            
            h3 {
                font-weight: normal;
                margin-bottom: 4px;
            }
            
            p {
                margin-bottom: 10px;
            }
            
            ul {
                list-style: none;
                margin-bottom: 10px;
            }
            
            ul li {
                display: inline-block;
            }
            
            ul.cards li {
                border: 1px solid #ccc;
                margin: 0px 2px;
            }
            
            ul.cards.small li {
                width: 30px;
                height: 30px;
            }
            
            ul.cards.large li img {
                width: 100px;
                height: auto;
            }

            ul.itemize li {
                padding: 5px;
                margin: 0px 2px;
                background-color: #066;
                color: #fff;
                font-weight: bold;
                font-size: small;
                -webkit-border-radius: 5px;
                -moz-border-radius: 5px;
                border-radius: 5px;
            }
            
            input[type=text] {
                width: 100%;
                padding: 8px 12px; 
                margin: 30px 0px;
                border: 1px solid #ccc; 
                box-shadow: -1px 1px 4px rgba(0, 0, 0, 0.1), inset -1px 1px 2px rgba(0, 0, 0, 0.1);
            }  

        </style>
    </head>
    <body>
        <!--<input id="descricao" type="text" placeholder="Descreva sua aplicacao" value="$description" />-->
        <h3>Descricao</h3>
        <p id="descricao">$description</p>
        
        <h3>Palavras-chave</h3>
        <ul id="palavras-chave" class="itemize">
            $keywords
        </ul>
        
        <h3>Cores</h3>
        <ul id="resultado" class="cards small">
            $colors
        </ul>
        
        <h3>Imagens</h3>
        <ul id="imagens" class="cards large">
            $images
        </ul>
    </body>
</html>