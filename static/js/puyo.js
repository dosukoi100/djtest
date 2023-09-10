/* ぷよぷよアニメーション */


/*document.querySelector(".square").animate(
    {
      //borderRadius: [
        //"50% 50% 50% 70%/50% 50% 70% 60%",
        //"80% 30% 50% 50%/50%",
        //"40% 40% 50% 40%/30% 50% 40% 80%"
      //]
      borderRadius: [
        "10% 20% 30% 40%/50% 50% 70% 60%",
        "80% 30% 50% 50%/50%",
        "40% 40% 50% 40%/30% 50% 40% 80%"
      ]
    },
    {
      iterations: Infinity,
      direction: "alternate",
      duration: 7000
    }
);
*/

//対象
const heading = document.querySelector('.square');

//動作
const keyframes = {
    /*borderRadius: [
        "10% 20% 30% 40%/50% 50% 70% 60%",
        "80% 30% 50% 50%/50%",
        "40% 40% 50% 40%/30% 50% 40% 80%"
    ],*/
    //四角形の丸みを変化させていく
    borderRadius: ['50%','100%','0%','50%'],
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

//動作状態
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

heading.animate(keyframes,status1);
