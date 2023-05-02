import React,{createContext, useState} from 'react';
export const Contex = createContext();
export const Provider = ({children})=>{
    const [client,setClient] = useState([]);
    const [user,setUser] = useState('')
    const [ruc, setRuc] = useState('');
    const [usuario, setUsuario] = useState('');
    const [productos,setProductos] = useState([])
   

    const globalContex = {
        user,setUser,
        ruc,setRuc,
        usuario,setUsuario,
        client,setClient,
        productos,setProductos,
        

    }
    
    return <Contex.Provider value={globalContex}>{children}</Contex.Provider>
};
