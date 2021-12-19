import React, {useState,useEffect} from 'react'
import ListItem from '../components/ListItem'
import AddButton from '../components/AddButton'
const NoteListPage = () => {

    let [items,setItems] = useState([])

    useEffect(() => {
        getItems()
    }, [])

    let getItems = async () => {
        let response = await fetch('/api/items/')
        let data = await response.json()
        console.log('DATA',data)
        setItems(data)
    }

    return (
        <div className="notes">
            <div className="note-header">
                <h2 className="notes-title">&#9782;</h2>
                <p className="notes-count">{items.length}</p>
            </div>
            <div className="items-list">
                {items.map((item,index) => (
                    <ListItem key={index} item={item}/>
                ))}
            </div>
            <AddButton/>
        </div>
    )
}

export default NoteListPage