import { useState, useCallback } from 'react';
import PageContainer from '../components/layout/PageContainer';
import Button from '../components/common/Button';
import DatePicker from '../components/planner/DatePicker';
import BudgetSelector from '../components/planner/BudgetSelector';
import TravelersSelector from '../components/planner/TravelersSelector';
import ThemeSelector from '../components/planner/ThemeSelector';
import DestinationSelector from '../components/planner/DestinationSelector';
import TripSummary from '../components/planner/TripSummary';
import ItineraryPlaceholder from '../components/planner/ItineraryPlaceholder';
import { generateTripPlan } from '../services/plannerService';

const TRAVEL_STYLE_MAP = {
  beach: 'relaxation',
  culture: 'culture',
  adventure: 'adventure',
  city: 'general',
  nature: 'general',
  food: 'food',
};

const GROUP_TYPE_MAP = {
  solo: 'solo',
  couple: 'couple',
  family: 'family',
  group: 'friends',
};

function mapRequest(tripData) {
  return {
    destination: tripData.destination,
    start_date: tripData.startDate,
    end_date: tripData.endDate,
    travel_style: TRAVEL_STYLE_MAP[tripData.theme] || 'general',
    budget_level: tripData.budget || 'moderate',
    group_type: GROUP_TYPE_MAP[tripData.travelers] || 'couple',
  };
}

export default function TripPlannerPage() {
  const [tripData, setTripData] = useState({
    destination: '',
    startDate: '',
    endDate: '',
    budget: '',
    travelers: '',
    theme: '',
  });
  const [plan, setPlan] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const updateField = (field, value) => {
    setTripData((prev) => ({ ...prev, [field]: value }));
    setPlan(null);
    setError(null);
  };

  const handleGenerate = useCallback(async () => {
    setLoading(true);
    setError(null);
    setPlan(null);
    try {
      const result = await generateTripPlan(mapRequest(tripData));
      setPlan(result);
    } catch (err) {
      setError(err.message || 'Failed to generate itinerary. Please try again.');
    } finally {
      setLoading(false);
    }
  }, [tripData]);

  const allFieldsFilled =
    tripData.destination &&
    tripData.startDate &&
    tripData.endDate &&
    tripData.budget &&
    tripData.travelers &&
    tripData.theme;

  return (
    <div className="bg-background py-8">
      <PageContainer>
        <div className="mb-8 text-center">
          <h1 className="text-3xl font-bold text-primary sm:text-4xl">
            Plan Your Trip
          </h1>
          <p className="mt-2 text-secondary">
            Tell us your preferences and we will create a personalized itinerary
          </p>
        </div>

        <div className="grid gap-8 lg:grid-cols-[1fr_320px]">
          {/* Main content */}
          <div className="space-y-8">
            <div className="rounded-card border border-border bg-surface p-6 shadow-card">
              <DestinationSelector
                selected={tripData.destination}
                onSelect={(val) => updateField('destination', val)}
              />
            </div>

            <div className="rounded-card border border-border bg-surface p-6 shadow-card">
              <DatePicker
                startDate={tripData.startDate}
                endDate={tripData.endDate}
                onStartChange={(val) => updateField('startDate', val)}
                onEndChange={(val) => updateField('endDate', val)}
              />
            </div>

            <div className="rounded-card border border-border bg-surface p-6 shadow-card">
              <BudgetSelector
                selected={tripData.budget}
                onSelect={(val) => updateField('budget', val)}
              />
            </div>

            <div className="rounded-card border border-border bg-surface p-6 shadow-card">
              <TravelersSelector
                selected={tripData.travelers}
                onSelect={(val) => updateField('travelers', val)}
              />
            </div>

            <div className="rounded-card border border-border bg-surface p-6 shadow-card">
              <ThemeSelector
                selected={tripData.theme}
                onSelect={(val) => updateField('theme', val)}
              />
            </div>

            {error && (
              <div className="rounded-card border border-border bg-surface p-6 shadow-card">
                <div className="flex flex-col items-center justify-center py-8 text-center">
                  <div className="mb-4 flex h-16 w-16 items-center justify-center rounded-full bg-highlight/10">
                    <svg
                      className="h-8 w-8 text-highlight"
                      fill="none"
                      viewBox="0 0 24 24"
                      stroke="currentColor"
                      aria-hidden="true"
                    >
                      <path
                        strokeLinecap="round"
                        strokeLinejoin="round"
                        strokeWidth={1.5}
                        d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"
                      />
                    </svg>
                  </div>
                  <h3 className="mb-2 text-lg font-semibold text-primary">
                    Generation failed
                  </h3>
                  <p className="mb-6 max-w-sm text-secondary">{error}</p>
                  <Button variant="primary" onClick={handleGenerate}>
                    Try Again
                  </Button>
                </div>
              </div>
            )}

            <div className="rounded-card border border-border bg-surface p-6 shadow-card">
              <ItineraryPlaceholder
                tripData={tripData}
                plan={plan}
                loading={loading}
                onGenerate={handleGenerate}
              />
            </div>
          </div>

          {/* Sidebar */}
          <div className="lg:sticky lg:top-24 lg:self-start">
            <TripSummary tripData={tripData} />

            <div className="mt-4">
              <Button
                variant="highlight"
                size="lg"
                className="w-full"
                onClick={handleGenerate}
                disabled={!allFieldsFilled || loading}
              >
                {loading ? 'Generating...' : 'Generate Itinerary'}
              </Button>
            </div>

            <div className="mt-6 rounded-card border border-border bg-surface p-4 shadow-card">
              <h4 className="mb-2 text-sm font-semibold text-primary">How it works</h4>
              <ol className="space-y-2 text-xs text-secondary">
                <li className="flex gap-2">
                  <span className="font-semibold text-accent">1.</span>
                  Choose your destination
                </li>
                <li className="flex gap-2">
                  <span className="font-semibold text-accent">2.</span>
                  Set your travel dates
                </li>
                <li className="flex gap-2">
                  <span className="font-semibold text-accent">3.</span>
                  Pick your budget and group size
                </li>
                <li className="flex gap-2">
                  <span className="font-semibold text-accent">4.</span>
                  Select a travel theme
                </li>
                <li className="flex gap-2">
                  <span className="font-semibold text-accent">5.</span>
                  Generate your personalized plan
                </li>
              </ol>
            </div>
          </div>
        </div>
      </PageContainer>
    </div>
  );
}
