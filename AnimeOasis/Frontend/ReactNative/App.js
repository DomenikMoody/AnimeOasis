import { StatusBar } from 'expo-status-bar';
import { SafeAreaView, StyleSheet, Text, View } from 'react-native';
import { Video, ResizeMode } from 'expo-av';

export default function App() {
  return (
    <SafeAreaView style={styles.container}>
      <Video
        style={styles.video}
        source={{
          uri: 'https://www002.vipanicdn.net/streamhls/0789fd4f049c3ca2a49b860ea5d1f456/ep.1.1677591537.480.m3u8',
        }}
      />
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
  video: {
    height: "100%",
    width: "100%"
  }
});
