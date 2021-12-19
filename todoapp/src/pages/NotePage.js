import React, {useState, useEffect} from 'react'
// import { Link } from 'react-router-dom';
import {ReactComponent as ArrowLeft} from '../assets/arrow-left.svg'
// import { withRouter } from 'react-router-dom'
// import { useParams } from 'react-router'

const NotePage = ({match,history}) => {

    let itemId = match.params.id
    let [item, setItem] = useState(null);
    
    useEffect(() => {
        getItem()
        // eslint-disable-next-line
    }, [itemId])

    let getItem =async()=>{
        console.log(itemId);
        if(itemId === 'new') return

        let response = await fetch(`/api/items/${itemId}/`)
        let data = await response.json()
        setItem(data)
    }
    let createItem = async () => {
        fetch(`/api/items/create`, {
            method: "POST",
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(item)
        })
    }

    let updateItem = async () => {
        fetch(`/api/items/${itemId}/update/`, {
            method: "PUT",
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(item)
        })
    }

    let deleteItem = async () => {
        fetch(`/api/items/${itemId}`,{
            method:"DELETE",
            'headers':{
                'Content-Type':'application/json'
                
            }
        })
        
        // eslint-disable-next-line
        history.push('/')
    }
    let handleSubmit = () => {
        console.log('ITEM:',item)
        if(itemId!=='new' && !item.title === ''){
            deleteItem()
        }else if(itemId!== 'new'){
            updateItem()
        }else if(itemId === 'new' && item !==null){
            createItem()
        }
        // eslint-disable-next-line
        history.push('/')
    }
    return (
        <div className="note">
            <div className="note-header">
                <h3>
                    <ArrowLeft onClick={handleSubmit}/>
                </h3>
                {itemId !== 'new' ? (
                    <button onClick={deleteItem}>Delete</button>
                ) : (
                    <button onClick={handleSubmit}>Done</button>
                )}
            </div>
            <textarea onChange={(e) => {setItem({ ...item,'title':e.target.value})}} defaultValue={item?.title}></textarea>
            </div>
        
    )
}

export default NotePage