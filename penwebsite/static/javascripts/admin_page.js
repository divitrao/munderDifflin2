$(document).ready(function(){
    document.body.onload = create_image

    function create_image(){
        for(i=1;i<=2;i++){
        const newDiv = document.createElement("div")
        newDiv.setAttribute('id','image_class')

        const image_block = document.createElement("img")

        image_block.src = "{conts.img"+i+".url}}"

        image_block.setAttribute('id','image'+i)

        newDiv.appendChild(image_block)

        document.getElementById('content-box').appendChild(newDiv)

       

        const current_div = document.getElementById('name_pen')

        document.body.insertBefore(newDiv,current_div)
    }
}

    $("#change_pic").click(()=>{
        // alert("hi")
        $("#images").attr('src','/media/images/background.jpg')
    })
})