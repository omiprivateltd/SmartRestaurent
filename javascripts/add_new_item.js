function collect_item_info() { 
    let item_name = document.querySelector("#Item_name_value").value
    let item_price = document.querySelector("#item_price").value
    let item_description = document.querySelector("#item_description").value
    let item_image = document.querySelector("#item_image")
    form_data = new FormData()
    form_data.append("item_name",item_name)
    form_data.append("item_price",item_price)
    form_data.append("item_description",item_description)
    form_data.append("image_data",item_image.files[0])
    let backend_api_url = "http://127.0.0.1:8000/addItem"
    fetch(backend_api_url,{method:"POST",body:form_data}).then(response =>alert(response)).catch(console.error)}   

function remove_item() { 
    let item_name_to_remvoe = document.querySelector("#item_name_value").value
    api_endpoint = "http://127.0.0.1:8000/deleteItem?itemName="+item_name_to_remvoe
    fetch(api_endpoint,{method:"POST"})
    alert("ITEM REMOVED")
}