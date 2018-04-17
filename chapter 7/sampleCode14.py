def on_data(self, data):
        def transform(key, value):
            return transforms[key](value) if key in transforms else value
        data = self.enrich(json.loads(data))
        if data is not None:
            self.buffered_data.append(
                {key:transform(key,value) \
                     for key,value in iteritems(data) \
                     if key in fieldnames}
            )
            self.flush_buffer_if_needed()
        return True
