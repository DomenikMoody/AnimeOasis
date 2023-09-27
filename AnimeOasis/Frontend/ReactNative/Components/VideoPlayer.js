import { View, Text, SafeAreaView} from "react-native";
import Video from 'react-native-video'

const VidPlayer = () => {
    return (
        <SafeAreaView>
            <Text>
                THIS IS WHERE THE VIDEO PLAYER WOULD BE
            </Text>
            <Video
            source= {{uri: "https://www002.vipanicdn.net/streamhls/0789fd4f049c3ca2a49b860ea5d1f456/ep.1.1677591537.480.m3u8"}}
            >
            </Video>
        </SafeAreaView>
    )
}

export default VidPlayer
