import { FlatList} from "react-native";
import {DUMMY_DATA} from '../../data/dummy'
import { RefreshControl } from "react-native-gesture-handler";
import { EventItemClient } from "./event-item-client";


export const EventListClient = ({data})=>{
    const renderItem = ({item})=>{
    
        return <EventItemClient id={item.id} nombre={item.nombre} apellido={item.apellido} razon_social = {item.razon_social} ruc={item.ruc} direccion = {item.direccion}/>
    }
    return (
     
            <FlatList
            data = {data}
            keyExtractor={item=>item.id}
            renderItem={renderItem}
            
            refreshControl={
                <RefreshControl
                refreshing={false}
                onRefresh={()=>console.log('refresh')}
                />
            }
            />
         
    
    );
}