import { useContext } from "react";
import {Contex} from "../../screen/context"
import { View } from "react-native";
export const EditVentaProduct = (data)=>{
    const globalContex = useContext(Contex)
    const {productos }= globalContex;
    retun (
        <View>
            <Text>Edicion de un porducto de  venta</Text>
        </View>
    );
}