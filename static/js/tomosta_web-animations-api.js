//ともすた簡単Web Animations API

'use strict';

//id属性headingのもが対象(querySelectorをかける)として変数を定義
const heading = document.querySelector('#heading');

//対象に対するアニメーション動作部分の指定(CSSのセレクタ的)
const keyframes = {
    //文字色
    color: ['red','yellow','blue','green','purple'],
    //不透明度:0透明 1不透明
    opacity: [0.5,1,0.5],
    //背景色
    background: ['blue'],
    //トランスレート(移動)
    //大括弧内は第一引数は開始値第二引数は終了値(x,y)座標
    translate: ['-100px 400px','100px 300px','-100px 200px','100px 100px',0]
};


//アニメーションの状態を指示する変数
const status1 = {
    //動作時間の指定
    duration: 10000,
    //色、トランスレートの動作を降順の後昇順にする
    direction: 'alternate',
    //*動作を断続的の行う指定
    iterations: Infinity,
    //最初と最後の動作をゆっくりにする
    easing: 'ease'
};

//headingに対してanimate()メソッドでアニメーションを実行
//第一引数に動作、第二引数に状態を指定(default 変化の時間durationの指定)
heading.animate(keyframes,status1);

//練習 関数化した連続再生
/*
function playseq() {
    heading.animate(keyframes,10000).onfinish = function() {
        playseq();
    }
};

playseq();
*/


//どすこいフュージョン
const opt = document.querySelector('#opt');

const opt_keys = {
    color: ['red','yellow','blue','green','purple'],
    //不透明度:0透明 1不透明
    opacity: [0.35,1,0.35],
    //背景色
    background: ['red'],
    //トランスレート(移動)
    //大括弧内は第一引数は開始値第二引数は終了値(x,y)座標
    translate: ['0px 300px','0px 0px']
};

opt.animate(opt_keys,10000);

