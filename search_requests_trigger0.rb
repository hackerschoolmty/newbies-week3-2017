class SearchRequestsTrigger
  include Sidekiq::Worker

  sidekiq_options :queue => :search

  def perform(id)    
    request = MongoSearch.find(id)
    request.connect_and_try_to_search
  end
end
