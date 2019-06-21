#!/usr/bin/env python
# -*- coding: utf-8 -*-

style = '''
	<style type="text/css">
	.Fundo {
    flex: 1;
    align-items: center;
    justify-items: center
}

    html{
    background-color: #E3F6CE;
    }

.Titulo {
    flex: 1;
    justify-content: center;
    align-items: center;
    justify-items: center;
    text-align: center;
    text-justify: auto
}

.Conteudo {
    display: flex;
    width: 99vw;
    height: 90vh;
    border: 1px solid #000;
    overflow: auto;
    flex-direction: row;
    justify-content: space-around
}

.Vitaminas {
    display: flex;
    padding: 10px;
    width: 68vw;
    height: 80vh;
    overflow: auto;
    flex-direction: row;
    flex-wrap: wrap;
}

h4{
    text-align: center;
    width: 100%;
    font-size: 15px;
    margin: 0px;
}

h5{
    text-align: center;
    width: 100%;
    font-size: 17px;
    margin-top: 5px;
    margin-bottom: 5px;
}

h6{
    text-align: center;
    width: 100%;
    font-size: 14px;
    font-weight: 100;
    margin: 0px;
}

p{
    text-align: justify;
    font-size: 13px;
    
}

.botao{
    display: flex;
    height: 8vh;
    width: 10vw;
    justify-content: center;
    align-items: center;
    background-color: #5FB404;
    font-size: 20px;
    color: white;
}

.divBotao{
    display: flex;
    width: 100%;
    justify-content: center;
    align-items: center;
}

.consumidos{
    font-size: 15px;
}

.VitaminasItem {
    display: flex;
    padding: 5px;
    margin: 5px;
    width: 20vw;
    height: 18vh;
    overflow: auto;
    flex-wrap: wrap;
    flex-direction: row;
    border: 1px solid #BCF5A9;
    background-color: #BCF5A9;

}

.Dicas {
    width: 30vw;
    height: 99%;
    overflow: auto;
    border: 1px solid #90EE90;
    
}


.DicasItem {
    display: flex;
    padding: 5px;
    margin: 5px;
    width: 100%;
    overflow: auto;
    flex-wrap: wrap;
    flex-direction: row;
    border: 1px solid #5FB404;
    
}
.fonte{
    font-size: 10px;
}

.Dicas::-webkit-scrollbar-track {
    background-color: #F4F4F4;
}
.Dicas::-webkit-scrollbar {
    width: 6px;
    background: #F4F4F4;
}
.Dicas::-webkit-scrollbar-thumb {
    background: #dad7d7;
}

.DicasItem::-webkit-scrollbar-track {
    background-color: #F4F4F4;
}
.DicasItem::-webkit-scrollbar {
    width: 6px;
    background: #F4F4F4;
}
.DicasItem::-webkit-scrollbar-thumb {
    background: #dad7d7;
}

.VitaminasItem::-webkit-scrollbar-track {
    background-color: #F4F4F4;
}
.VitaminasItem::-webkit-scrollbar {
    width: 6px;
    background: #F4F4F4;
}
.VitaminasItem::-webkit-scrollbar-thumb {
    background: #dad7d7;
}

.Vitaminas::-webkit-scrollbar-track {
    background-color: #F4F4F4;
}
.Vitaminas::-webkit-scrollbar {
    width: 6px;
    background: #F4F4F4;
}
.Vitaminas::-webkit-scrollbar-thumb {
    background: #dad7d7;
}
		</style>
	'''