import { FlatList} from "react-native";
import {DUMMY_DATA} from '../../data/dummy'
import { RefreshControl } from "react-native-gesture-handler";
import { EventItem } from "./event-item-product";


export const EventListProduc = ({data})=>{
    const renderItem = ({item})=>{
    
        return <EventItem id={item.id} producto={item.producto} descripcion={item.descripcion} precio = {item.precio} stock={item.stock} descuento = {item.descuento}/>
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