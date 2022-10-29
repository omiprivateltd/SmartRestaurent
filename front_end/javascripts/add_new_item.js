function collect_item_info() { 
    let item_name = document.querySelector("#Item_name_value").value
    let item_price = document.querySelector("#item_price").value
    let item_description = document.querySelector("#item_description").value
    let item_image = document.querySelector("#item_image")
    // image to array 
    // const file = item_image.files[0];
    // const reader = new FileReader()
    // item_image.addEventListener('change',e => {
        
    //     ;
    //     reader.addEventListener('load',()=>{ console.log(reader.result) } )
    //     console.log(reader.readAsDataURL(file))
    //     alert(reader.readAsDataURL(file)) }
    //      )
    // console.log(item_name,item_price,item_description,item_image)
    // console.log("data url",reader.readAsDataURL(file))
    let backend_api_url = "https://localhost:8080"
    let json_object = {"item_name":item_name,"item_price":item_price,"item_description":item_description,"item_image_array":item_image_array}
    fetch(backend_api_url,{})
  }   