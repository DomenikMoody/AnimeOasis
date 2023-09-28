import { StatusBar } from 'expo-status-bar';
import { SafeAreaView, StyleSheet, Text, View } from 'react-native';
import { Video, ResizeMode } from 'expo-av';
import VidPlayer from './Components/VideoPlayer';

export default function App() {
  return (
    <SafeAreaView >
      <Text>Words Here !!!!!!!</Text>
      <VidPlayer />
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
