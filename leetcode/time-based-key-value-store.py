class TimeMap {

    HashMap<String, TreeMap<Integer, String>> map;

    // first string -> key
    // second string in tree map -> value
    // integer -> timestamp

    public TimeMap() {
        map = new HashMap<>();
    }

    public void set(String key, String value, int timestamp) {
        if (!map.containsKey(key)) {
            map.put(key, new TreeMap<>());
        }

        TreeMap<Integer, String> submap = map.get(key);

        submap.put(timestamp, value);
    }

    public String get(String key, int timestamp) {
        if (!map.containsKey(key)) {
            return "";
        }

        TreeMap<Integer, String> submap = map.get(key);

        Integer prevtimestamp = submap.floorKey(timestamp);

        if (prevtimestamp == null)
            return "";

        return submap.get(prevtimestamp);
    }
}

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap obj = new TimeMap();
 * obj.set(key,value,timestamp);
 * String param_2 = obj.get(key,timestamp);
 */