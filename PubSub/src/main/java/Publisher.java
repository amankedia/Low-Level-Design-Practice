public interface Publisher {
    void publish(Message message, PubSubService pubSubService);
}
