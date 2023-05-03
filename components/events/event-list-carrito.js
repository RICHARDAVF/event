import { FlatList } from "react-native";

const EvenListCarrito = ()=>{
    const renderItem = ()=>{
        return <EventCarrito />
    }
    return (
        <FlatList 
        keyExtractor={item=>item.id}
        renderItem={ renderItem}
        />
    );

}