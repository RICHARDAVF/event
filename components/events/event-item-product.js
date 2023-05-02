import { useNavigation } from "@react-navigation/native";
import { TouchableOpacity,Text,StyleSheet,View} from "react-native";


export const EventItem = ({id,producto,descripcion,precio,stock,descuento})=>{
    const navigation = useNavigation()
    return (
        // <TouchableOpacity style={styles.card} onPress={()=>{navigation.navigate('Event',{eventId:[id,title,descripcion]})}}>
        <TouchableOpacity style={styles.card} onPress={()=>{navigation.navigate('Event',{eventId:id})}} >
            <View style={styles.container}>
            <View style={styles.column}>
                <Text>ID: {id}</Text>
                <Text>Producto: {producto}</Text>
                <Text>Descripción: {descripcion}</Text>
            </View>
            <View style={styles.column}>
                <Text>Precio: {precio}</Text>
                <Text>Stock: {stock}</Text>
                <Text>Descuento: {descuento}</Text>
            </View>
            </View>
        </TouchableOpacity>
    );
}

const styles = StyleSheet.create({
    card:{
        borderWidth:1,
        borderColor:'gray',
        borderRadius:10,
        marginVertical:5,
        padding:30,
        
    },
    container: {
        flexDirection: 'row',
        justifyContent: 'space-between',
        paddingVertical: 10,
      },
    column: {
        flex: 1,}
});