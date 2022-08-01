let video = document.querySelector("#webcam1");

if (navigator.mediaDevices.getUserMedia){
    navigator.mediaDevices.getUserMedia({video:true})
    .then(function(stream){
        video.srcObject = stream;
    })
    .catch(function(err){
        console.log("something went wrong")
    })
} else {
    console.log("gum not supported");
}

let video2 = document.querySelector("#webcam2");

if (navigator.mediaDevices.getUserMedia){
    navigator.mediaDevices.getUserMedia({video:true})
    .then(function(stream){
        video2.srcObject = stream;
    })
    .catch(function(err){
        console.log("something went wrong")
    })
} else {
    console.log("gum not supported");
}

let video3 = document.querySelector("#webcam3");

if (navigator.mediaDevices.getUserMedia){
    navigator.mediaDevices.getUserMedia({video:true})
    .then(function(stream){
        video3.srcObject = stream;
    })
    .catch(function(err){
        console.log("something went wrong");
    })
} else {
    console.log("gum not supported");
}

let click_img = document.querySelector("#click_img");

click_img.addEventListener('click',()=>{

    var canvas = document.getElementById("canvas");
    var context = canvas.getContext("2d");
    context.drawImage(video2,0,0,640,480);

    b64_img = canvas.toDataURL();
    console.log(b64_img);

    passive_liveness(document.getElementById("login_id").textContent,b64_img);
});


function passive_liveness(email , b64_img){

   
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "http://127.0.0.1:5000/demo/test_passive_liveness", true);
    xhr.setRequestHeader('Content-Type', 'application/json');

    xhr.onload = function(){ 
      if(this.status.toString() == "200"){
          document.getElementById("log_form").reset();
          alert("Job Created");
      }else{
          alert("Error Creating Job");
      }
    };
    xhr.send(JSON.stringify({
        "email":email,
        "b64_img":b64_img
    }));
   
    return false;
}
