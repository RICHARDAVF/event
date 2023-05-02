import React,{createContext, useState} from 'react';
export const Contex = createContext();
export const Provider = ({children})=>{
   
    const [user,setUser] = useState('')
    const [ruc, setRuc] = useState('');
    const [usuario, setUsuario] = useState('');
   

    const globalContex = {
        user,setUser,
        ruc,setRuc,
        usuario,setUsuario,
        
        

    }
    
    return <Contex.Provider value={globalContex}>{children}</Contex.Provider>
};
