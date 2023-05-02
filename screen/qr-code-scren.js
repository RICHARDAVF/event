
import { View ,Text,StyleSheet} from "react-native";

export const QrCodeScreen = ()=>{
    return(
        <View style={styles.scren}>
            <Text>QR SCAN</Text>
        </View>
    );
}
const styles = StyleSheet.create({
    scren:{
        padding:20
    }
});