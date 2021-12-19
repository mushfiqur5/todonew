import React from 'react'
import { Link } from 'react-router-dom'



let getTitle=(item)=> {
    let title=item.title.split('\n')[0]
    if(title.length>45){
        return title.slice(0,45)
    }
    return title
}

const ListItem = ({item}) => {
    return (
        <Link to={`/item/${item.id}`}>
            <div className="notes-list-item">
            <h1>Title : {getTitle(item)}</h1>
            
            <p>Created at : <span>{item.created}</span></p>
            <p>Updated at : <span>{item.updated}</span></p>
            </div>
        </Link>
    )
}

export default ListItem